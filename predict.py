#!/usr/bin/env python3
"""
Cats and Dogs Image Classifier - Prediction Script

This script loads the trained model and makes predictions on new images.
Usage: python predict.py <image_path> [image_path2] [image_path3] ...
"""

import sys
import os
import numpy as np
import tensorflow as tf
from PIL import Image
import argparse


def load_model(model_path='my_model.keras'):
    """Load the trained model from file."""
    try:
        model = tf.keras.models.load_model(model_path)
        print(f"Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)


def preprocess_image(image_path, target_size=(128, 128)):
    """
    Preprocess an image for prediction.
    
    Args:
        image_path (str): Path to the image file
        target_size (tuple): Target size for resizing (width, height)
    
    Returns:
        numpy.ndarray: Preprocessed image ready for prediction
    """
    try:
        # Load image using PIL
        image = Image.open(image_path)
        
        # Convert to RGB if needed (handles RGBA, grayscale, etc.)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Resize to target size
        image = image.resize(target_size)
        
        # Convert to numpy array
        image_array = np.array(image)
        
        # Normalize pixel values to [0, 1]
        image_array = image_array / 255.0
        
        # Add batch dimension
        image_array = np.expand_dims(image_array, axis=0)
        
        return image_array
        
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None


def predict_image(model, image_path):
    """
    Make prediction on a single image.
    
    Args:
        model: Loaded Keras model
        image_path (str): Path to the image file
    
    Returns:
        dict: Prediction results with class name and confidence
    """
    # Preprocess the image
    processed_image = preprocess_image(image_path)
    
    if processed_image is None:
        return None
    
    # Make prediction
    try:
        prediction = model.predict(processed_image, verbose=0)
        
        # Convert prediction to class (0 = cat, 1 = dog)
        confidence = float(prediction[0][0])
        
        if confidence > 0.5:
            predicted_class = "dog"
            class_confidence = confidence
        else:
            predicted_class = "cat"
            class_confidence = 1 - confidence
        
        return {
            'image_path': image_path,
            'predicted_class': predicted_class,
            'confidence': class_confidence,
            'raw_prediction': confidence
        }
        
    except Exception as e:
        print(f"Error making prediction for {image_path}: {e}")
        return None


def main():
    """Main function to handle command line arguments and make predictions."""
    parser = argparse.ArgumentParser(
        description='Predict whether images contain cats or dogs using the trained model.'
    )
    parser.add_argument(
        'images', 
        nargs='+', 
        help='Path(s) to image file(s) to classify'
    )
    parser.add_argument(
        '--model', 
        default='my_model.keras',
        help='Path to the trained model file (default: my_model.keras)'
    )
    
    args = parser.parse_args()
    
    # Check if model file exists
    if not os.path.exists(args.model):
        print(f"Error: Model file '{args.model}' not found.")
        print("Please ensure you have trained the model and saved it as 'my_model.keras'")
        print("or specify the correct path using --model argument.")
        sys.exit(1)
    
    # Load the model
    model = load_model(args.model)
    
    print(f"\nMaking predictions on {len(args.images)} image(s)...")
    print("-" * 60)
    
    # Process each image
    for image_path in args.images:
        if not os.path.exists(image_path):
            print(f"❌ Image not found: {image_path}")
            continue
        
        result = predict_image(model, image_path)
        
        if result is None:
            print(f"❌ Failed to process: {image_path}")
            continue
        
        # Display results
        class_emoji = "🐱" if result['predicted_class'] == 'cat' else "🐶"
        confidence_percent = result['confidence'] * 100
        
        print(f"{class_emoji} {os.path.basename(image_path)}")
        print(f"   Prediction: {result['predicted_class'].upper()}")
        print(f"   Confidence: {confidence_percent:.1f}%")
        print()


if __name__ == "__main__":
    main()