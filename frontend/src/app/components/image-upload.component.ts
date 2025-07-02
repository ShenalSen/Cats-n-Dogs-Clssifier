import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PredictionService, PredictionResponse } from '../services/prediction.service';

@Component({
  selector: 'app-image-upload',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-12">
          <h1 class="text-4xl font-bold text-gray-900 mb-4 animate-fade-in">
            🐱 Cats & Dogs Classifier 🐶
          </h1>
          <p class="text-xl text-gray-600 animate-slide-up">
            Upload an image and let AI determine if it's a cat or dog!
          </p>
          <div class="mt-4 flex justify-center">
            <div class="flex items-center space-x-2">
              <div class="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
              <span class="text-sm text-gray-500">{{serverStatus}}</span>
            </div>
          </div>
        </div>

        <!-- Upload Area -->
        <div class="mb-8">
          <div 
            class="relative border-2 border-dashed border-gray-300 rounded-lg p-12 text-center hover:border-gray-400 transition-colors duration-200 animate-bounce-in"
            [class.border-blue-400]="isDragOver"
            [class.bg-blue-50]="isDragOver"
            (dragover)="onDragOver($event)"
            (dragleave)="onDragLeave($event)"
            (drop)="onDrop($event)">
            
            <div class="space-y-4">
              <div class="mx-auto h-12 w-12 text-gray-400">
                <svg fill="none" stroke="currentColor" viewBox="0 0 48 48">
                  <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <div>
                <label for="file-upload" class="cursor-pointer">
                  <span class="mt-2 block text-sm font-medium text-gray-900">
                    Drag and drop your image here, or 
                    <span class="text-blue-600 hover:text-blue-500">browse</span>
                  </span>
                </label>
                <input 
                  id="file-upload" 
                  name="file-upload" 
                  type="file" 
                  class="sr-only" 
                  accept="image/*"
                  (change)="onFileSelected($event)">
              </div>
              <p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
            </div>
          </div>
        </div>

        <!-- Selected Image Preview -->
        <div *ngIf="selectedImage" class="mb-8 animate-slide-up">
          <div class="bg-white rounded-lg shadow-lg p-6">
            <h3 class="text-lg font-medium text-gray-900 mb-4">Selected Image</h3>
            <div class="flex flex-col md:flex-row gap-6">
              <div class="flex-1">
                <img 
                  [src]="selectedImage" 
                  alt="Selected image" 
                  class="w-full h-64 object-cover rounded-lg shadow-md">
              </div>
              <div class="flex-1 flex flex-col justify-center">
                <button 
                  (click)="predict()"
                  [disabled]="isLoading"
                  class="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-bold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105 disabled:transform-none animate-pulse-glow">
                  <span *ngIf="!isLoading">🔮 Predict</span>
                  <span *ngIf="isLoading" class="flex items-center justify-center">
                    <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Analyzing...
                  </span>
                </button>
                <button 
                  (click)="clearImage()"
                  class="mt-3 bg-gray-300 hover:bg-gray-400 text-gray-700 font-bold py-2 px-6 rounded-lg transition-colors duration-200">
                  Clear Image
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Prediction Result -->
        <div *ngIf="prediction" class="mb-8 animate-bounce-in">
          <div class="bg-white rounded-lg shadow-lg p-6" [class.animate-shake]="showErrorAnimation">
            <h3 class="text-lg font-medium text-gray-900 mb-4">Prediction Result</h3>
            <div class="text-center">
              <div class="text-6xl mb-4">
                {{ prediction.predicted_class === 'cat' ? '🐱' : '🐶' }}
              </div>
              <h4 class="text-2xl font-bold mb-2" 
                  [class.text-purple-600]="prediction.predicted_class === 'cat'"
                  [class.text-orange-600]="prediction.predicted_class === 'dog'">
                It's a {{ prediction.predicted_class | titlecase }}!
              </h4>
              <div class="mb-4">
                <p class="text-gray-600 mb-2">Confidence Level</p>
                <div class="w-full bg-gray-200 rounded-full h-3">
                  <div 
                    class="h-3 rounded-full transition-all duration-1000 ease-out"
                    [class.bg-purple-500]="prediction.predicted_class === 'cat'"
                    [class.bg-orange-500]="prediction.predicted_class === 'dog'"
                    [style.width.%]="prediction.confidence * 100">
                  </div>
                </div>
                <p class="text-sm text-gray-500 mt-1">
                  {{ (prediction.confidence * 100) | number:'1.1-1' }}% confident
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Error Message -->
        <div *ngIf="errorMessage" class="mb-8 animate-shake">
          <div class="bg-red-50 border border-red-200 rounded-lg p-4">
            <div class="flex">
              <div class="flex-shrink-0">
                <svg class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
                </svg>
              </div>
              <div class="ml-3">
                <h3 class="text-sm font-medium text-red-800">Error</h3>
                <p class="mt-2 text-sm text-red-700">{{ errorMessage }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Tips -->
        <div class="bg-white rounded-lg shadow-lg p-6 animate-fade-in">
          <h3 class="text-lg font-medium text-gray-900 mb-4">💡 Tips for best results</h3>
          <ul class="space-y-2 text-gray-600">
            <li class="flex items-center">
              <span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>
              Use clear, well-lit images
            </li>
            <li class="flex items-center">
              <span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>
              Make sure the cat or dog is the main subject
            </li>
            <li class="flex items-center">
              <span class="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>
              Images should be at least 128x128 pixels
            </li>
          </ul>
        </div>
      </div>
    </div>
  `,
  styles: []
})
export class ImageUploadComponent {
  selectedImage: string | null = null;
  selectedFile: File | null = null;
  isDragOver = false;
  isLoading = false;
  prediction: PredictionResponse | null = null;
  errorMessage: string | null = null;
  showErrorAnimation = false;
  serverStatus = 'Checking server...';

  constructor(private predictionService: PredictionService) {
    this.checkServerHealth();
  }

  checkServerHealth() {
    this.predictionService.checkHealth().subscribe({
      next: (response) => {
        this.serverStatus = response.model_loaded ? 'Server ready ✅' : 'Server starting...';
      },
      error: () => {
        this.serverStatus = 'Server offline ❌';
      }
    });
  }

  onDragOver(event: DragEvent) {
    event.preventDefault();
    this.isDragOver = true;
  }

  onDragLeave(event: DragEvent) {
    event.preventDefault();
    this.isDragOver = false;
  }

  onDrop(event: DragEvent) {
    event.preventDefault();
    this.isDragOver = false;
    
    const files = event.dataTransfer?.files;
    if (files && files.length > 0) {
      this.handleFile(files[0]);
    }
  }

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.handleFile(input.files[0]);
    }
  }

  handleFile(file: File) {
    if (!file.type.startsWith('image/')) {
      this.showError('Please select an image file');
      return;
    }

    if (file.size > 10 * 1024 * 1024) { // 10MB limit
      this.showError('File size must be less than 10MB');
      return;
    }

    this.selectedFile = file;
    this.errorMessage = null;
    this.prediction = null;

    // Create preview
    const reader = new FileReader();
    reader.onload = (e) => {
      this.selectedImage = e.target?.result as string;
    };
    reader.readAsDataURL(file);
  }

  predict() {
    if (!this.selectedFile) return;

    this.isLoading = true;
    this.errorMessage = null;
    this.prediction = null;

    this.predictionService.predictFromFile(this.selectedFile).subscribe({
      next: (response) => {
        this.prediction = response;
        this.isLoading = false;
      },
      error: (error) => {
        this.showError('Failed to get prediction. Please check if the server is running.');
        this.isLoading = false;
      }
    });
  }

  clearImage() {
    this.selectedImage = null;
    this.selectedFile = null;
    this.prediction = null;
    this.errorMessage = null;
  }

  showError(message: string) {
    this.errorMessage = message;
    this.showErrorAnimation = true;
    setTimeout(() => {
      this.showErrorAnimation = false;
    }, 820);
  }
}