from django.urls import path,include
from .views import updateCover,updateOtherInfos

urlpatterns = [
    path('updateCoverPhoto/',updateCover),
    path('updateOtherInfos',updateOtherInfos)
]
