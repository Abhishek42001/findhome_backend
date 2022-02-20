from django.urls import path,include
from .views import ApplyBookmark

urlpatterns = [
    path('',ApplyBookmark)
]
