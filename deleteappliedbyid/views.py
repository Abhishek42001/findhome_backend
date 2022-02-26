from django.shortcuts import render
from apply.models import Apply
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def deletebyid(request):
    id=request.data.get('id')
    x=Apply.objects.filter(id=id).delete()
    print(x)
    return Response({"message":"Deletion Successful"},status=200)