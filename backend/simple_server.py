#!/usr/bin/env python3
import http.server
import socketserver
import json
import urllib.parse
import random
import time
from http import HTTPStatus

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()

    def do_GET(self):
        if self.path == '/health':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "healthy",
                "model_loaded": True
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/predict' or self.path == '/predict_base64':
            # Simulate processing time
            time.sleep(1)
            
            # Mock prediction
            is_dog = random.choice([True, False])
            confidence = random.uniform(0.7, 0.95)
            
            if is_dog:
                predicted_class = "dog"
            else:
                predicted_class = "cat"
                confidence = 1 - confidence
            
            response = {
                "predicted_class": predicted_class,
                "confidence": float(confidence),
                "raw_prediction": confidence if is_dog else 1 - confidence
            }
            
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()

if __name__ == "__main__":
    PORT = 5000
    
    print(f"Starting Mock Cats & Dogs Classifier API on port {PORT}...")
    print("Note: This is a mock version for testing the frontend.")
    
    with socketserver.TCPServer(("", PORT), CORSHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print("Health check: http://localhost:5000/health")
        httpd.serve_forever()