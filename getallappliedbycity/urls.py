from django.urls import path,include
from .views import Getappliedbycity

urlpatterns = [
    path('',Getappliedbycity)
]