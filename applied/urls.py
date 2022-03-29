from django.urls import path,include
from .views import GetApplied,updateApplied

urlpatterns = [
    path('',GetApplied),
    path('updateApplied/',updateApplied),
]
