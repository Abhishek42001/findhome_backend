from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ApplyBookmarkSerializer
# Create your views here.

@api_view(['POST'])
def ApplyBookmark(request):
    data=request.data
    serializer=ApplyBookmarkSerializer(data=data)
    if not serializer.is_valid():
        return Response({"status":400,"message":serializer.errors})
    serializer.save()
    return Response({"status":200,"message":"Bookmarked Successfully..."})
