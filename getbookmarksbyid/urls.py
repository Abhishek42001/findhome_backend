from django.urls import path,include
from .views import GetBookmarksbyid

urlpatterns = [
    path('',GetBookmarksbyid)
]