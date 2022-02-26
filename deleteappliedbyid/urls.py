from django.urls import path,include
from .views import deletebyid

urlpatterns = [
    path('',deletebyid)
]