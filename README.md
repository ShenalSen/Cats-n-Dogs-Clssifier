# Cats and Dogs Image Classifier

This repository contains an implementation of a deep learning-based image classifier for distinguishing between images of cats and dogs. The model is built using TensorFlow and leverages a pre-trained Xception model for transfer learning.

## Features
- **Dataset**: The project uses the [Cats and Dogs dataset](https://www.kaggle.com/datasets/dineshpiyasamara/cats-and-dogs-for-classification) from Kaggle.
- **Data Preprocessing**: Images are resized to `128x128` and normalized for optimal training.
- **Transfer Learning**: Incorporates the Xception model pre-trained on ImageNet as the feature extractor.
- **Custom Layers**: Adds custom dense layers to fine-tune the classification task.
- **Performance Metrics**: Tracks accuracy, precision, and recall during evaluation.

## Project Structure
- `image_classifier_t_learning.ipynb`: The main notebook containing all the code for downloading data, preprocessing, model building, training, and evaluation.
- `my_model.keras`: (Generated after training) The saved model for deployment or further use.
- `predict.py`: Standalone script for making predictions on new images using the trained model.
- `example_usage.py`: Example script demonstrating programmatic usage of the prediction functionality.
- `requirements.txt`: List of required Python packages.

## Getting Started

### Prerequisites
- Python 3.x
- Kaggle API credentials for downloading the dataset.

### Required Libraries
Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

Or install them individually:
```bash
pip install numpy pandas matplotlib tensorflow pillow
```

### Steps to Run the Notebook
1. Clone this repository:
   ```bash
   git clone https://github.com/ShenalSen/Cats-n-Dogs-Clssifier.git
   cd Cats-n-Dogs-Clssifier
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the `image_classifier_t_learning.ipynb` notebook.
4. Provide Kaggle credentials to download the dataset.
5. Execute the cells step-by-step to preprocess the data, train the model, and evaluate its performance.

### Making Predictions on New Images
After training the model, you can use the prediction script to classify new images:

```bash
# Predict a single image
python predict.py path/to/your/image.jpg

# Predict multiple images
python predict.py image1.jpg image2.png image3.jpeg

# Use a different model file
python predict.py --model custom_model.keras image.jpg
```

The script will output the prediction (cat or dog) and confidence level for each image.

#### Example Output:
```
🐱 cat_photo.jpg
   Prediction: CAT
   Confidence: 94.2%

🐶 dog_photo.jpg
   Prediction: DOG
   Confidence: 87.6%
```

## Highlights

### Model Architecture
- **Base Model**: Xception (pre-trained on ImageNet).
- **Custom Layers**:
  - Flatten
  - Dense (128 units, ReLU)
  - Dense (128 units, ReLU)
  - Dense (32 units, ReLU)
  - Dense (1 unit, Sigmoid)

### Training and Evaluation
- **Epochs**: 3
- **Batch Size**: 32
- **Performance**:
  - Loss and accuracy are plotted for both training and validation sets.
  - Evaluation metrics include precision, recall, and accuracy.

### Dataset Splits
- Training: 90% of the dataset.
- Validation: 10% of the training set.
- Testing: Separate test set.

## Results
- Achieved high accuracy in classifying cats and dogs.
- Precision: ~97.8%
- Recall: ~90.4%
- Accuracy: ~94.2%

## Future Work
- Experiment with different architectures and hyperparameters.
- Extend the classifier to other animal datasets.
- Deploy the model as a web service or application.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
