from multiprocessing import context
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ApplySerializer, ApplywithImagesSerializer
from rest_framework.response import Response
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Apply
import base64
# Create your views here.

@api_view(['POST'])
def apply(request):
    parser_classes = (MultiPartParser, FormParser)
    data=request.data
    print("from view:",request.data)
    serializer=ApplySerializer(data=data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({"status":400,"message":serializer.errors})
    id_obj=serializer.create(validated_data=data)
    # images=data.getlist(key='images')
    # for image in images:
    #     print(image)
    #     temp=ApplywithImagesSerializer(data={"user_details":id_obj.id,"images":image})
    #     if temp.is_valid():
    #         temp.save()
    #     else:
    #         return Response({"status":400,"message":temp.errors})
    print("successs")
    return Response({"status":200,"message":"Data Successfully Inserted"})
