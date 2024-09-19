
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('result/', views.result, name='result'),
    path('',views.home_view,name='home')
    ]
