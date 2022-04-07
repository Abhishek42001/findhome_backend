from django.urls import path,include
from .views import updateCover

urlpatterns = [
    path('updateCoverPhoto/',updateCover)
]
