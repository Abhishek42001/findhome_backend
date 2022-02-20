from django.urls import path,include
from .views import findappliedbyid

urlpatterns = [
    path('',findappliedbyid)
]
