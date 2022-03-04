from django.urls import path,include
from .views import sendmessage

urlpatterns = [
    path('',sendmessage)
]