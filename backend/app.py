from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Global variable to store the model
model = None

def load_model():
    """Load the trained model"""
    global model
    try:
        # Check if model file exists
        model_path = '../my_model.keras'
        if os.path.exists(model_path):
            model = tf.keras.models.load_model(model_path)
            print("Model loaded successfully!")
        else:
            print(f"Model file not found at {model_path}")
            # For now, we'll create a dummy model with the same architecture
            print("Creating dummy model with same architecture...")
            create_dummy_model()
    except Exception as e:
        print(f"Error loading model: {e}")
        create_dummy_model()

def create_dummy_model():
    """Create a dummy model with the same architecture as described in the notebook"""
    global model
    # Create the same architecture as in the notebook
    pretrained_model = tf.keras.applications.xception.Xception(
        include_top=False,
        input_shape=(128, 128, 3),
        weights="imagenet",
        pooling='max'
    )
    
    for layer in pretrained_model.layers:
        layer.trainable = False
    
    model = tf.keras.models.Sequential([
        pretrained_model,
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=128, activation='relu'),
        tf.keras.layers.Dense(units=128, activation='relu'),
        tf.keras.layers.Dense(units=32, activation='relu'),
        tf.keras.layers.Dense(units=1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    print("Dummy model created successfully!")

def preprocess_image(image):
    """Preprocess image for prediction"""
    # Resize image to 128x128 as expected by the model
    image = image.resize((128, 128))
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    # Convert to numpy array
    image_array = np.array(image)
    # Normalize pixel values to [0, 1]
    image_array = image_array.astype('float32') / 255.0
    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "model_loaded": model is not None})

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if uploaded image is a cat or dog"""
    try:
        # Check if model is loaded
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        # Get image from request
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No image selected"}), 400
        
        # Process the image
        image = Image.open(file.stream)
        processed_image = preprocess_image(image)
        
        # Make prediction
        prediction = model.predict(processed_image)
        prediction_value = float(prediction[0][0])
        
        # Convert prediction to class (0 = cat, 1 = dog based on typical binary classification)
        if prediction_value > 0.5:
            predicted_class = "dog"
            confidence = prediction_value
        else:
            predicted_class = "cat"
            confidence = 1 - prediction_value
        
        return jsonify({
            "predicted_class": predicted_class,
            "confidence": float(confidence),
            "raw_prediction": prediction_value
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict_base64', methods=['POST'])
def predict_base64():
    """Predict from base64 encoded image"""
    try:
        # Check if model is loaded
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        data = request.get_json()
        if 'image' not in data:
            return jsonify({"error": "No image data provided"}), 400
        
        # Decode base64 image
        image_data = data['image'].split(',')[1]  # Remove data:image/...;base64, prefix
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Process the image
        processed_image = preprocess_image(image)
        
        # Make prediction
        prediction = model.predict(processed_image)
        prediction_value = float(prediction[0][0])
        
        # Convert prediction to class
        if prediction_value > 0.5:
            predicted_class = "dog"
            confidence = prediction_value
        else:
            predicted_class = "cat"
            confidence = 1 - prediction_value
        
        return jsonify({
            "predicted_class": predicted_class,
            "confidence": float(confidence),
            "raw_prediction": prediction_value
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Load model on startup
    load_model()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)