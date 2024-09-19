import tensorflow as tf
import numpy as np
import os
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm

# Singleton pattern for TensorFlow model

class ModelSingleton:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = tf.keras.models.load_model('classifier/static/models/model_land_use.h5')
        return cls._model


def home(request):
    return render(request, 'home.html')

def classify_image(image_path):
    model = ModelSingleton.get_model()
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    categories=['sparseresidential', 'parkinglot', 'river', 'overpass', 'storagetanks', 'runway', 'tenniscourt', 'mobilehomepark', 'mediumresidential', 'intersection', 'chaparral', 'denseresidential', 'golfcourse', 'buildings', 'forest', 'harbor', 'freeway', 'beach', 'baseballdiamond', 'airplane', 'agricultural']
    class_index =categories[np.argmax(prediction[0])]
    return class_index

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            uploaded_file_path = fs.url(filename)
            
            # Convert the URL path to an absolute path
            absolute_file_path = os.path.join('media', filename)
            
            # Classify image
            class_index = classify_image(absolute_file_path)
            
            return render(request, 'classifier/result.html', {
                'uploaded_file_url': fs.url(filename),
                'class_index': class_index
            })
    else:
        form = ImageUploadForm()

    return render(request, 'classifier/upload.html', {'form': form})

def result(request):
    return render(request, 'classifier/result.html')


def home_view(request):
    return render(request,'classifier/home.html')
    