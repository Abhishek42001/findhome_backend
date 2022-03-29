from django.urls import path,include
from .views import update

urlpatterns = [
    path('',update)
]
