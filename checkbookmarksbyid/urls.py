from django.urls import path,include
from .views import Checkbookmarksbyid

urlpatterns = [
    path('',Checkbookmarksbyid)
]
