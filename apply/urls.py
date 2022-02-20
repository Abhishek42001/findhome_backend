from django.urls import path,include
from .views import apply

urlpatterns = [
    path('',apply)
]