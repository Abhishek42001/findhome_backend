from django.urls import path,include
from .views import updateCover,updateOtherInfos,deleteAdditionalPhotos,uploadAdditionalPhotos

urlpatterns = [
    path('updateCoverPhoto/',updateCover),
    path('updateOtherInfos/',updateOtherInfos),
    path('deleteAdditionalPhotos/',deleteAdditionalPhotos),
    path('uploadAdditionalPhotos/',uploadAdditionalPhotos)
]
