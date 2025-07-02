#!/usr/bin/env python3
"""
Demo script for the Cats and Dogs Classifier
This script demonstrates how to use the prediction system.
"""

import os
import sys
from PIL import Image
import numpy as np

def create_sample_images():
    """Create sample images for demonstration."""
    print("Creating sample images for demonstration...")
    
    # Create a cat-like image (brownish)
    cat_img = Image.new('RGB', (200, 150), color=(139, 69, 19))  # Brown color
    cat_img.save('demo_cat.jpg')
    print("✓ Created demo_cat.jpg")
    
    # Create a dog-like image (grayish)
    dog_img = Image.new('RGB', (200, 150), color=(128, 128, 128))  # Gray color
    dog_img.save('demo_dog.jpg')
    print("✓ Created demo_dog.jpg")
    
    return ['demo_cat.jpg', 'demo_dog.jpg']

def main():
    """Main demo function."""
    print("🐱🐶 Cats and Dogs Classifier Demo")
    print("=" * 40)
    
    # Check if model exists
    if not os.path.exists('my_model.keras'):
        print("\n⚠️  Model file 'my_model.keras' not found!")
        print("Please follow these steps:")
        print("1. Run the Jupyter notebook 'image_classifier_t_learning.ipynb'")
        print("2. Train the model and save it as 'my_model.keras'")
        print("3. Then run this demo again")
        print("\nAlternatively, you can test with any other .keras model file:")
        print("python predict.py --model your_model.keras demo_cat.jpg")
        return
    
    # Create sample images
    sample_images = create_sample_images()
    
    print(f"\n🔍 Making predictions...")
    print("Run the following command to test:")
    print(f"python predict.py {' '.join(sample_images)}")
    
    print("\n📝 Other usage examples:")
    print("python predict.py your_cat_photo.jpg")
    print("python predict.py *.jpg *.png")
    print("python predict.py --model custom_model.keras image.jpg")
    
    print("\n🔧 For programmatic usage, see example_usage.py")
    print("python example_usage.py")
    
    print("\n🎯 Expected output format:")
    print("🐱 demo_cat.jpg")
    print("   Prediction: CAT")
    print("   Confidence: XX.X%")
    print()
    print("🐶 demo_dog.jpg")
    print("   Prediction: DOG")
    print("   Confidence: XX.X%")

if __name__ == "__main__":
    main()