from django.urls import path,include
from .views import GetApplied

urlpatterns = [
    path('',GetApplied)
]
