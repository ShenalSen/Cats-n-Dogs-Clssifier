# Running the Cats & Dogs Classifier Web App

## Quick Start Guide

### Step 1: Start the Backend
```bash
cd backend
python3 simple_server.py
```

You should see:
```
Starting Mock Cats & Dogs Classifier API on port 5000...
Note: This is a mock version for testing the frontend.
Server running at http://localhost:5000
Health check: http://localhost:5000/health
```

### Step 2: Start the Frontend
```bash
cd frontend
npm install  # First time only
npm start
```

You should see:
```
✔ Building...
Watch mode enabled. Watching for file changes...
  ➜  Local:   http://localhost:4200/
```

### Step 3: Use the Application
1. Open your browser to `http://localhost:4200`
2. You'll see a beautiful interface with:
   - Header with title "🐱 Cats & Dogs Classifier 🐶"
   - Server status indicator
   - Drag-and-drop upload area
   - Tips section

3. Upload an image by:
   - Dragging and dropping an image file
   - Clicking "browse" to select a file

4. Click "Predict" to get the classification result

5. View results with:
   - Predicted class (Cat 🐱 or Dog 🐶)
   - Confidence percentage with animated progress bar
   - Smooth animations throughout

## Features Showcase

### 🎨 Advanced Animations
- **Fade-in**: Title and tips sections
- **Slide-up**: Image preview and results
- **Bounce-in**: Results card with spring effect
- **Pulse**: Server status indicator
- **Glow**: Predict button with pulsing glow
- **Shake**: Error messages with attention-grabbing shake
- **Smooth transitions**: All hover effects and state changes

### 📱 Responsive Design
- Works on desktop, tablet, and mobile
- Flexible grid layout adapts to screen size
- Touch-friendly drag-and-drop

### 🔧 API Integration
- Real-time server health checking
- File upload support
- Base64 image encoding support
- Error handling with user feedback

## File Structure
```
├── backend/
│   ├── simple_server.py      # Mock API server (Python 3 only)
│   ├── app.py               # Full Flask server (requires Flask + TensorFlow)
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/app/components/
│   │   └── image-upload.component.ts  # Main UI component
│   ├── src/app/services/
│   │   └── prediction.service.ts      # API service
│   └── src/styles.css       # Custom Tailwind-inspired styles
└── README_WEBAPP.md         # Detailed documentation
```

The application demonstrates modern web development practices with Angular and provides an intuitive interface for machine learning model interaction.