from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ApplyBookmarkSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ApplyBookmark as Applymodel,Item_id 
# Create your views here.

@api_view(['POST'])
def ApplyBookmark(request):
    parser_classes = (MultiPartParser, FormParser)
    data=request.data
    if Applymodel.objects.filter(user_id=data.getlist('user_id')[0]).exists() and Item_id.objects.filter(item_id=data.getlist('item_id')[0]).exists():
        return Response({"status":200,"message":"Already Bookmarked"})
    serializer=ApplyBookmarkSerializer(data=data)
    if not serializer.is_valid():
        return Response({"status":400,"message":serializer.errors})
    # print(serializer.create(validated_data=data))
    return Response({"status":200,"message":"Bookmarked Successfully..."})
