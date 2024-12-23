**Project Objective**
This project focuses on classifying satellite images into specific land use categories. A Convolutional Neural Network (CNN) model was trained and tested to achieve accurate classifications. The project includes the implementation of the trained model as a web application using Django.

**Dataset Information**
The dataset used contains satellite images categorized into various land use types.
Images were resized to 150x150 pixels for uniformity.
Each image is associated with a label denoting its category (e.g., urban, forest, water).

**Technologies Used**
_-->>Model Development:_
Python
TensorFlow/Keras
NumPy
OpenCV

_-->>Web Application:_
Django
PIL (Python Imaging Library)

**Steps Involved**
_1. Data Preparation_
-Images were preprocessed by resizing to 150x150 pixels.
-Data normalization was applied by scaling pixel values to the range [0, 1].

_2. Model Training_
-A CNN was built and trained on the dataset using TensorFlow/Keras.
-The architecture includes convolutional, pooling, and fully connected layers.
-The model was saved as model_land_use.h5 after training.

_3. Model Evaluation_
-The model was evaluated using standard metrics such as accuracy.
-Predictions were validated on a separate test set to ensure robustness.

_4. Web Application Development_
-Django was used to create a robust and scalable web application.
-Users can upload images, which are processed and classified into one of the predefined categories.

**How to Use the Application**
_1.Setup_
  -Ensure Python and required libraries (TensorFlow, Django, PIL, OpenCV, NumPy) are installed.
  -Place the trained model file (model_land_use.h5) in the project directory.
_2.Run the Application_
  -Start the Django development server using the command: 
  -python manage.py runserver
_3.Classify Images_
  -Access the application via the local server URL (e.g., http://127.0.0.1:8000).
  -Upload a satellite image (JPG, JPEG, or PNG format).
  -View the predicted category displayed on the interface.

**Code Explanation**
_Core Functions_

1.preprocess_image(image):
-Converts the uploaded image into a format compatible with the model.
-Resizes the image to 150x150 pixels, normalizes pixel values, and adds a batch dimension.

2.predict_image(image):
-Passes the preprocessed image to the CNN model for prediction.
-Maps the model's output to the corresponding category label.

**Django Views**
-Handles image upload and processing.
-Passes the processed image to the prediction function and renders the result in the HTML template.

**Results and Observations**
-The CNN achieved high accuracy in classifying the test set.
-The Django app provides a user-friendly interface for end users.
-Model predictions align well with expected outcomes, demonstrating the effectiveness of the preprocessing and training pipeline.

**Future Enhancements**
_1.Improve Model Performance_
  -Experiment with advanced architectures (e.g., ResNet, EfficientNet).
  -Use data augmentation to improve generalization.

_2.Expand Categories_
  -Include more diverse land use categories.
  -Train on larger datasets.

_3.Web Application Features_
  -Add confidence scores for predictions.
  -Enable batch uploads for multiple image classification.

**Dependencies**
-Python 3.x
-TensorFlow/Keras
-NumPy
-OpenCV
-Django
-PIL

**Conclusion**
This project successfully demonstrates the use of CNNs for satellite image classification and the integration of machine learning models into web applications using Django. The implementation provides a practical tool for analyzing satellite images and serves as a foundation for further enhancements.

