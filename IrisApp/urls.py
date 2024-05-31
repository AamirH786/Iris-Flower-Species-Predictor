# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Predictor, name='Predict'),
    path('result/', views.FormInfo, name='Info'),
]
