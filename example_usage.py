#!/usr/bin/env python3
"""
Example usage of the Cats and Dogs prediction functionality.

This script demonstrates how to use the prediction functions programmatically.
"""

import os
from predict import load_model, predict_image


def predict_batch(image_paths, model_path='my_model.keras'):
    """
    Predict multiple images at once.
    
    Args:
        image_paths (list): List of paths to image files
        model_path (str): Path to the trained model file
    
    Returns:
        list: List of prediction results
    """
    # Load model once
    model = load_model(model_path)
    
    results = []
    for image_path in image_paths:
        if os.path.exists(image_path):
            result = predict_image(model, image_path)
            if result:
                results.append(result)
        else:
            print(f"Warning: Image not found: {image_path}")
    
    return results


def example_usage():
    """Example of how to use the prediction functions."""
    
    # Check if model exists
    if not os.path.exists('my_model.keras'):
        print("Model file 'my_model.keras' not found.")
        print("Please train the model first using the Jupyter notebook.")
        return
    
    print("Example: Programmatic usage of the cats and dogs classifier")
    print("=" * 60)
    
    # Example image paths (these would be real image files)
    example_images = [
        'cat_example.jpg',
        'dog_example.jpg',
        'pet_photo.png'
    ]
    
    # Filter to only existing files
    existing_images = [img for img in example_images if os.path.exists(img)]
    
    if not existing_images:
        print("No example images found. To test the classifier:")
        print("1. Add some cat/dog images to this directory")
        print("2. Use the command line: python predict.py your_image.jpg")
        return
    
    # Make predictions
    results = predict_batch(existing_images)
    
    # Display results
    for result in results:
        print(f"Image: {result['image_path']}")
        print(f"Prediction: {result['predicted_class']}")
        print(f"Confidence: {result['confidence']:.2%}")
        print("-" * 30)


if __name__ == "__main__":
    example_usage()