import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ImageUploadComponent } from './components/image-upload.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ImageUploadComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected title = 'Cats & Dogs Classifier';
}
