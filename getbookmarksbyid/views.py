from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from applybookmark.serializer import ApplyBookmarkSerializer
from applybookmark.models import ApplyBookmark


# Create your views here.

@api_view(['POST'])
def GetBookmarksbyid(request):
    data=request.data['user_id']
    data=ApplyBookmark.objects.filter(user_id=data)
    serializer=ApplyBookmarkSerializer(data,many=True)
    return Response({"status":200,"data":serializer.data})
