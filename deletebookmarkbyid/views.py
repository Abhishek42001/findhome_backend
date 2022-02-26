from django.shortcuts import render
from applybookmark.models import ApplyBookmark as Applymodel,Item_id
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

@api_view(['POST'])
def Delete(request):
    parser_classes = (MultiPartParser, FormParser)
    data=request.data
    if not len(Applymodel.objects.filter(user_id=data.getlist('user_id')[0])[0].ss.filter(item_id=data.getlist('item_id')[0])):
        return Response({"status":200,"value":"Sorry Item Not Found"})
    print(len(Applymodel.objects.filter(user_id=data.getlist('user_id')[0])[0].ss.filter(item_id=data.getlist('item_id')[0])))
    print(Applymodel.objects.filter(user_id=data.getlist('user_id')[0])[0].ss.filter(item_id=data.getlist('item_id')[0]).delete())
    # if Item_id.objects.filter(item_id=data.getlist('item_id')[0]).exists():
    #     Item_id.objects
    #     return Response({"status":200,"value":True})
    return Response({"status":200,"value":"Deleted Successfully"})
