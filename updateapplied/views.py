from django.shortcuts import render
from apply.models import Apply
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

#incomplete


@api_view(['POST'])
def update(request):
    print(request.data)
    if "name" in request.data:
        print("ss")
    return Response({"status":200,"message":"Success"})
 