import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface PredictionResponse {
  predicted_class: string;
  confidence: number;
  raw_prediction: number;
}

@Injectable({
  providedIn: 'root'
})
export class PredictionService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  predictFromFile(file: File): Observable<PredictionResponse> {
    const formData = new FormData();
    formData.append('image', file);
    
    return this.http.post<PredictionResponse>(`${this.apiUrl}/predict`, formData);
  }

  predictFromBase64(base64Image: string): Observable<PredictionResponse> {
    const data = { image: base64Image };
    return this.http.post<PredictionResponse>(`${this.apiUrl}/predict_base64`, data);
  }

  checkHealth(): Observable<any> {
    return this.http.get(`${this.apiUrl}/health`);
  }
}