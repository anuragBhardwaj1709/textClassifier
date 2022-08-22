from django.urls import path
from . import views

urlpatterns = [
    path('TextClassifier/', views.Classifier.as_view(), name='classifier')
]
