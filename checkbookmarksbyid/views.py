from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from applybookmark.models import ApplyBookmark as Applymodel,Item_id 

# Create your views here.

@api_view(['POST'])
def Checkbookmarksbyid(request):
    parser_classes = (MultiPartParser, FormParser)
    data=request.data
    if Applymodel.objects.filter(user_id=data.getlist('user_id')[0]).exists() and Item_id.objects.filter(item_id=data.getlist('item_id')[0]).exists():
        return Response({"status":200,"value":True})
    return Response({"status":200,"value":False})
