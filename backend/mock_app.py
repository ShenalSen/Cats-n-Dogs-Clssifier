from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import base64
import io
from PIL import Image
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "model_loaded": True})

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if uploaded image is a cat or dog (mock prediction for now)"""
    try:
        # Get image from request
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No image selected"}), 400
        
        # Simulate processing time
        import time
        time.sleep(1)
        
        # Mock prediction - randomly choose cat or dog
        is_dog = random.choice([True, False])
        confidence = random.uniform(0.7, 0.95)
        
        if is_dog:
            predicted_class = "dog"
        else:
            predicted_class = "cat"
            confidence = 1 - confidence  # Invert confidence for cat
        
        return jsonify({
            "predicted_class": predicted_class,
            "confidence": float(confidence),
            "raw_prediction": confidence if is_dog else 1 - confidence
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict_base64', methods=['POST'])
def predict_base64():
    """Predict from base64 encoded image (mock prediction for now)"""
    try:
        data = request.get_json()
        if 'image' not in data:
            return jsonify({"error": "No image data provided"}), 400
        
        # Simulate processing time
        import time
        time.sleep(1)
        
        # Mock prediction - randomly choose cat or dog
        is_dog = random.choice([True, False])
        confidence = random.uniform(0.7, 0.95)
        
        if is_dog:
            predicted_class = "dog"
        else:
            predicted_class = "cat"
            confidence = 1 - confidence  # Invert confidence for cat
        
        return jsonify({
            "predicted_class": predicted_class,
            "confidence": float(confidence),
            "raw_prediction": confidence if is_dog else 1 - confidence
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Mock Cats & Dogs Classifier API...")
    print("Note: This is a mock version. Install TensorFlow to enable real predictions.")
    app.run(debug=True, host='0.0.0.0', port=5000)