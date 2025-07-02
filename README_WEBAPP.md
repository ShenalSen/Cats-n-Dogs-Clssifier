# Cats & Dogs Classifier Web Application

This project provides an interactive web interface for the Cats and Dogs image classifier using Angular frontend and Flask backend.

## Features

- **Interactive UI**: Modern, responsive interface with drag-and-drop image upload
- **Advanced Animations**: Smooth transitions and engaging visual feedback
- **Real-time Predictions**: Get instant predictions on uploaded images
- **Confidence Scoring**: See how confident the model is about its predictions
- **Cross-platform**: Works on desktop and mobile devices

## Project Structure

```
├── backend/
│   ├── app.py                 # Full Flask API with TensorFlow integration
│   ├── mock_app.py           # Mock API for testing without TensorFlow
│   └── requirements.txt      # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   │   └── image-upload.component.ts
│   │   │   ├── services/
│   │   │   │   └── prediction.service.ts
│   │   │   └── ...
│   │   └── styles.css        # Custom CSS with Tailwind-inspired utilities
│   └── ...
└── image_classifier_t_learning.ipynb  # Original ML model notebook
```

## Quick Start

### Backend Setup

1. **Option A: Mock Backend (for testing UI)**
   ```bash
   cd backend
   python3 mock_app.py
   ```

2. **Option B: Full Backend (requires TensorFlow)**
   ```bash
   cd backend
   pip install -r requirements.txt
   python3 app.py
   ```

### Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Run development server**
   ```bash
   npm start
   ```

3. **Build for production**
   ```bash
   npm run build
   ```

## Using the Application

1. **Start the backend** (choose mock or full version)
2. **Start the frontend** development server
3. **Open your browser** to `http://localhost:4200`
4. **Upload an image** by:
   - Dragging and dropping an image file
   - Clicking to browse and select a file
5. **Click "Predict"** to get the classification result
6. **View the results** with confidence score and visual feedback

## API Endpoints

### GET /health
Check server status and model availability.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### POST /predict
Upload an image file for prediction.

**Request:** Form data with 'image' file field

**Response:**
```json
{
  "predicted_class": "cat",
  "confidence": 0.85,
  "raw_prediction": 0.15
}
```

### POST /predict_base64
Send base64 encoded image for prediction.

**Request:**
```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ..."
}
```

**Response:**
```json
{
  "predicted_class": "dog",
  "confidence": 0.92,
  "raw_prediction": 0.92
}
```

## Model Information

- **Architecture**: Xception (pre-trained on ImageNet) + custom dense layers
- **Input Size**: 128x128 pixels
- **Classes**: Cat (0) and Dog (1)
- **Performance**: ~94.2% accuracy, ~97.8% precision, ~90.4% recall

## Development Notes

- The frontend uses custom CSS utilities inspired by Tailwind CSS
- Animations include fade-in, slide-up, bounce-in, and pulse effects
- The backend supports both file upload and base64 image formats
- CORS is enabled for cross-origin requests during development

## Future Improvements

- Add support for batch predictions
- Implement model confidence thresholding
- Add more animal categories
- Deploy to cloud platforms
- Add user authentication and history