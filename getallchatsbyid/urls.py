from django.urls import path,include
from .views import GetallChats

urlpatterns = [
    path('',GetallChats)
]