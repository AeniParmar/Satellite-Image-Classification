# **Satellite Image Classification - README**

## **Project Objective**  
This project aims to classify satellite images into specific land-use categories. A Convolutional Neural Network (CNN) was trained and integrated into a web application using Django for real-world usability.  

---

## **Dataset Information**  
- **Source**: The dataset contains satellite images categorized by land-use types such as urban, forest, and water.  
- **Image Preprocessing**:  
  - Resized to 150x150 pixels.  
  - Normalized to scale pixel values between 0 and 1.  
- **Categories**: Includes predefined labels for each image, indicating its type.  

---

## **Technologies Used**  

### **Model Development**  
- **Libraries**: TensorFlow/Keras, NumPy, OpenCV  
- **Techniques**:  
  - Convolutional Neural Networks (CNNs) for image classification  
  - Data preprocessing for scaling and resizing  

### **Web Application**  
- **Framework**: Django  
- **Utilities**: PIL (Python Imaging Library) for image handling  

---

## **Steps Involved**  

### **1. Data Preparation**  
- Resized all images to 150x150 pixels for consistency.  
- Applied normalization for efficient model training.  

### **2. Model Training**  
- Built and trained a CNN using TensorFlow/Keras.  
- Architecture includes convolutional, pooling, and fully connected layers.  
- Saved the trained model as `model_land_use.h5`.  

### **3. Model Evaluation**  
- Evaluated performance on the test set using accuracy and loss metrics.  
- Observed high accuracy in predictions.  

### **4. Web Application Development**  
- Developed a Django-based web application for user interaction.  
- Implemented functionality to upload images and classify them.  

---

## **How to Use the Application**  

### **Setup**  
1. Clone the repository to your local machine:  
   ```bash  
   git clone <https://github.com/AeniParmar/Satellite-Image-Classification.git>  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Place the trained model file (`model_land_use.h5`) in the project directory.  

### **Run the Application**  
1. Start the Django development server:  
   ```bash  
   python manage.py runserver  
   ```  
2. Access the application via your browser at `http://127.0.0.1:8000`.  

### **Classify an Image**  
1. Upload a satellite image (formats: JPG, PNG, JPEG).  
2. View the classification results displayed on the application interface.  

---

## **Key Features**  

### **Core Functions**  
1. **`preprocess_image(image)`**:  
   - Resizes and normalizes the uploaded image for prediction.  

2. **`predict_image(image)`**:  
   - Feeds the processed image to the CNN model.  
   - Outputs the corresponding land-use category.  

### **User Interface**  
- A simple, intuitive web page for uploading images and viewing results.  

---

## **Results & Observations**  
- High classification accuracy with the trained CNN.  
- The web application provides seamless integration and usability.  
- Model predictions align effectively with the dataset labels.  

---

## **Future Enhancements**  
1. **Model Improvements**:  
   - Experiment with advanced architectures like ResNet or EfficientNet.  
   - Use larger datasets and data augmentation techniques.  
2. **Application Features**:  
   - Add confidence scores for predictions.  
   - Support bulk uploads for multiple image classification.  

---

## **Dependencies**  
- Python 3.x  
- TensorFlow/Keras  
- NumPy  
- OpenCV  
- Django  
- PIL  

---

## **Contributors**  
- **Aeni Parmar**  
  Data Analyst | [GitHub](https://github.com/AeniParmar)  

---
