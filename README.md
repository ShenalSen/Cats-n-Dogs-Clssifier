# Cats & Dogs Classifier - Web Application & ML Model

This repository contains a complete image classification solution with both a **modern web application** and the underlying **machine learning model** for distinguishing between images of cats and dogs. The project features an **Angular frontend** with **Python Flask backend**, built on a TensorFlow model using transfer learning with the pre-trained Xception architecture.

## 🌟 What's Included

- **🌐 Web Application**: Interactive Angular frontend with Python Flask backend
- **🧠 ML Model**: Deep learning classifier using TensorFlow and transfer learning  
- **📓 Jupyter Notebook**: Complete model development and training process
- **🔧 Multiple Backend Options**: Full TensorFlow integration or lightweight mock server

## 🚀 Quick Start - Web Application

### Prerequisites
- **Frontend**: Node.js and npm
- **Backend**: Python 3.x

### Run the Web Application
1. **Start the Backend** (Mock version for quick testing):
   ```bash
   cd backend
   python3 simple_server.py
   ```

2. **Start the Frontend**:
   ```bash
   cd frontend
   npm install    # First time only
   npm start
   ```

3. **Open your browser** to `http://localhost:4200` and start classifying images!

For detailed setup instructions, see [QUICK_START.md](QUICK_START.md) or [README_WEBAPP.md](README_WEBAPP.md).

## 🏗️ Architecture

### Web Application Stack
- **Frontend**: Angular 20.0.0 with modern responsive UI, drag-and-drop upload, and smooth animations
- **Backend**: Python Flask API with CORS support and TensorFlow integration
- **ML Model**: Xception-based classifier with custom dense layers
- **API**: RESTful endpoints for image upload and prediction

### Machine Learning Features
- **Dataset**: [Cats and Dogs dataset](https://www.kaggle.com/datasets/dineshpiyasamara/cats-and-dogs-for-classification) from Kaggle
- **Data Preprocessing**: Images resized to `128x128` and normalized  
- **Transfer Learning**: Xception model pre-trained on ImageNet as feature extractor
- **Custom Architecture**: Additional dense layers for fine-tuned classification
- **Performance**: ~94.2% accuracy, ~97.8% precision, ~90.4% recall

## 📁 Project Structure

```
├── 🌐 Web Application
│   ├── frontend/                    # Angular 20.0.0 application
│   │   ├── src/app/components/      # UI components (image upload, etc.)
│   │   ├── src/app/services/        # API services for backend communication
│   │   ├── src/styles.css          # Custom Tailwind-inspired styling
│   │   ├── package.json            # Node.js dependencies
│   │   └── README.md               # Angular-specific documentation
│   ├── backend/                     # Python Flask API servers
│   │   ├── app.py                  # Full Flask API with TensorFlow integration
│   │   ├── mock_app.py             # Mock API for testing without TensorFlow
│   │   ├── simple_server.py        # Lightweight HTTP server for quick testing
│   │   └── requirements.txt        # Python dependencies (Flask, TensorFlow, etc.)
│   ├── README_WEBAPP.md            # Detailed web application documentation
│   └── QUICK_START.md              # Quick start guide for the web app
│
├── 🧠 Machine Learning Model
│   ├── image_classifier_t_learning.ipynb  # Main ML notebook (training & evaluation)
│   ├── my_model.keras              # Saved trained model (generated after training)
│   ├── predict.py                  # Standalone prediction script
│   ├── example_usage.py            # Example usage of prediction functionality
│   ├── demo.py                     # Demo script with examples
│   └── requirements.txt            # ML-specific dependencies
│
└── 📋 Testing & Utilities
    ├── test_api.py                 # API testing utilities
    └── LICENSE                     # MIT License
```

## 🔧 Development Setup

### For Web Application Development

#### Backend Options
1. **Quick Mock Server** (No TensorFlow required):
   ```bash
   cd backend
   python3 simple_server.py
   ```

2. **Mock Flask API** (Testing Flask features):
   ```bash
   cd backend
   python3 mock_app.py
   ```

3. **Full Production API** (Requires TensorFlow):
   ```bash
   cd backend
   pip install -r requirements.txt
   python3 app.py
   ```

#### Frontend Development
```bash
cd frontend
npm install                 # Install dependencies
npm start                   # Development server (http://localhost:4200)
npm run build              # Production build
npm test                   # Run tests
```

### For ML Model Development

#### Prerequisites for ML Development
- Python 3.x
- Kaggle API credentials for downloading the dataset

#### Install ML Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install numpy pandas matplotlib tensorflow pillow
```

#### Run the ML Pipeline
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ShenalSen/Cats-n-Dogs-Clssifier.git
   cd Cats-n-Dogs-Clssifier
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Open and run the Jupyter notebook**:
   - Open `image_classifier_t_learning.ipynb`
   - Provide Kaggle credentials to download the dataset
   - Execute cells step-by-step to train and evaluate the model

## 🎯 Using the Trained Model

### Web Interface
After starting both backend and frontend servers, visit `http://localhost:4200` to:
- Upload images via drag-and-drop or file browser
- Get instant predictions with confidence scores
- Enjoy smooth animations and responsive design

### Command Line Predictions
Use the prediction script to classify images from the command line:

```bash
# Predict a single image
python predict.py path/to/your/image.jpg

# Predict multiple images  
python predict.py image1.jpg image2.png image3.jpeg

# Use a different model file
python predict.py --model custom_model.keras image.jpg
```

#### Example Output:
```
🐱 cat_photo.jpg
   Prediction: CAT
   Confidence: 94.2%

🐶 dog_photo.jpg
   Prediction: DOG
   Confidence: 87.6%
```

#### Quick Demo
```bash
python demo.py
```

## 🎨 Web Application Features

- **🖱️ Drag & Drop Upload**: Modern, intuitive image upload interface
- **⚡ Real-time Predictions**: Instant classification results
- **📊 Confidence Scoring**: Visual confidence indicators with animated progress bars  
- **🎭 Smooth Animations**: Engaging transitions and visual feedback
- **📱 Responsive Design**: Works seamlessly on desktop and mobile
- **🔄 Multiple Backend Support**: Choose between mock or full TensorFlow integration
- **🎯 Cross-platform**: Browser-based accessibility

## 🧠 Model Architecture & Performance

### Neural Network Design
- **Base Model**: Xception (pre-trained on ImageNet, frozen layers)
- **Custom Classification Head**:
  - Flatten layer
  - Dense (128 units, ReLU activation)
  - Dense (128 units, ReLU activation)  
  - Dense (32 units, ReLU activation)
  - Dense (1 unit, Sigmoid activation)

### Training Configuration
- **Input Size**: 128×128×3 (RGB images)
- **Epochs**: 3
- **Batch Size**: 32
- **Optimizer**: Adam
- **Loss Function**: Binary Crossentropy

### Dataset Information
- **Training Split**: 90% of the dataset
- **Validation Split**: 10% of the training set
- **Test Set**: Separate evaluation set
- **Classes**: Binary classification (Cat=0, Dog=1)

### Performance Metrics
- **🎯 Accuracy**: ~94.2%
- **🎯 Precision**: ~97.8%
- **🎯 Recall**: ~90.4%
- **📈 Training**: Loss and accuracy plotted for both training and validation sets

## 🔄 API Endpoints

The Flask backend provides RESTful API endpoints:

- **GET** `/health` - Health check and model status
- **POST** `/predict` - Upload image file for prediction
- **POST** `/predict_base64` - Send base64-encoded image for prediction

### Example API Usage
```bash
# Health check
curl http://localhost:5000/health

# Upload image for prediction
curl -X POST -F "image=@cat.jpg" http://localhost:5000/predict
```

## 🚀 Deployment Options

### Local Development
- Use `simple_server.py` for quick frontend testing
- Use `mock_app.py` for Flask development without TensorFlow
- Use `app.py` for full production-like testing

### Production Considerations
- Deploy frontend as static files to CDN/web server
- Deploy backend API to cloud platforms (AWS, GCP, Azure)
- Consider model optimization for faster inference
- Implement proper error handling and logging

## 🔮 Future Improvements

### Web Application Enhancements
- **👤 User Authentication**: Save prediction history and user preferences
- **📊 Batch Processing**: Upload and process multiple images simultaneously
- **🎛️ Model Confidence Thresholding**: Configurable confidence levels
- **🌍 Multi-language Support**: Internationalization for global users
- **📱 Mobile App**: Native iOS/Android applications
- **☁️ Cloud Deployment**: Deploy to AWS, GCP, or Azure with auto-scaling

### Model Improvements  
- **🐾 Extended Categories**: Support for more animal types beyond cats and dogs
- **🎯 Model Ensembling**: Combine multiple models for better accuracy
- **⚡ Model Optimization**: TensorFlow Lite for faster mobile inference
- **📈 Advanced Architectures**: Experiment with Vision Transformers, EfficientNet
- **🔄 Continuous Learning**: Online learning from user feedback

### Technical Enhancements
- **🧪 A/B Testing**: Test different UI/UX approaches
- **📊 Analytics Dashboard**: Monitor usage patterns and model performance  
- **🔒 Security**: Input validation, rate limiting, and secure file uploads
- **⚡ Caching**: Redis caching for frequently predicted images
- **📝 API Documentation**: OpenAPI/Swagger documentation

## 📚 Additional Resources

- **[README_WEBAPP.md](README_WEBAPP.md)** - Comprehensive web application documentation
- **[QUICK_START.md](QUICK_START.md)** - Step-by-step quick start guide
- **[frontend/README.md](frontend/README.md)** - Angular-specific development guide
- **[Kaggle Dataset](https://www.kaggle.com/datasets/dineshpiyasamara/cats-and-dogs-for-classification)** - Original training data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**🐱 Happy Classifying! 🐶**

*Built with ❤️ using Angular, Flask, and TensorFlow*

</div>
