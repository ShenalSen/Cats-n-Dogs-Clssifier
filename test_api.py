#!/usr/bin/env python3
"""
Simple test script to verify the backend API is working
"""
import requests
import json

def test_health_endpoint():
    """Test the health check endpoint"""
    try:
        response = requests.get('http://localhost:5000/health')
        print(f"Health check status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_prediction_endpoint():
    """Test the prediction endpoint with a dummy file"""
    try:
        # Create a dummy image file
        import io
        from PIL import Image
        
        # Create a simple test image
        img = Image.new('RGB', (128, 128), color='red')
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Send the image to the prediction endpoint
        files = {'image': ('test.jpg', img_bytes, 'image/jpeg')}
        response = requests.post('http://localhost:5000/predict', files=files)
        
        print(f"Prediction status: {response.status_code}")
        print(f"Prediction response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Prediction test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Cats & Dogs Classifier API...")
    print("=" * 50)
    
    health_ok = test_health_endpoint()
    print()
    
    if health_ok:
        prediction_ok = test_prediction_endpoint()
        print()
        
        if health_ok and prediction_ok:
            print("✅ All tests passed! API is working correctly.")
        else:
            print("❌ Some tests failed.")
    else:
        print("❌ Health check failed. Make sure the backend server is running.")
        
    print("\nTo start the backend server, run:")
    print("  cd backend && python3 simple_server.py")
    print("\nTo start the frontend, run:")
    print("  cd frontend && npm start")