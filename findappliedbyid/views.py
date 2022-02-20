from django.shortcuts import render
from rest_framework.response import Response
from apply.models import Apply
from apply.serializers import ApplySerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['POST'])
def findappliedbyid(request):
    data=request.data
    obs=Apply.objects.filter(user_id=data['user_id'])
    serializer=ApplySerializer(obs,many=True)
    return Response({"status":200,"data":serializer.data})
