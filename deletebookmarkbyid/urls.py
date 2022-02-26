from django.urls import path,include
from .views import Delete

urlpatterns = [
    path('',Delete),
]
