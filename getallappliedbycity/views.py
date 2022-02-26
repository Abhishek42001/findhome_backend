from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apply.models import Apply
from apply.serializers import ApplySerializer
# Create your views here.

@api_view(['GET'])
def Getappliedbycity(request):
    data=request.GET.get('city')
    # print(data)
    obs=Apply.objects.filter(city=str(data))
    serializer=ApplySerializer(obs,many=True)
    return Response({"data":serializer.data},status=200)
    