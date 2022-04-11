from django.urls import path,include
from .views import updateCover,updateOtherInfos,deleteAdditionalPhotos

urlpatterns = [
    path('updateCoverPhoto/',updateCover),
    path('updateOtherInfos/',updateOtherInfos),
    path('deleteAdditionalPhotos/',deleteAdditionalPhotos)
]
