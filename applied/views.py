from pty import CHILD
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apply.models import Apply,ApplywithImages
from apply.serializers import ApplySerializer,ApplywithImagesSerializer
# Create your views here.

@api_view(['GET'])
def GetApplied(request):
    obs=Apply.objects.all().order_by('-created_date')
    serializer=ApplySerializer(obs,many=True)
    return Response({"status":200,"data":serializer.data})

@api_view(['POST'])
def updateApplied(request):
    data=request.data
    Apply.objects.filter(user_id=data.getlist('user_id')[0]).update(
        profile_pic_url=data.getlist('profile_pic_url')[0]
    )
    return Response({"status":200,"data":"Successfully Updated"})