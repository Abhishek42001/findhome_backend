from django.urls import path,include
from .views import Getallchatsbtwntwo

urlpatterns = [
    path('',Getallchatsbtwntwo)
]
