from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from applybookmark.serializer import ApplyBookmarkSerializer
from applybookmark.models import ApplyBookmark
from apply.models import Apply
from apply.serializers import ApplySerializer


# Create your views here.

@api_view(['POST'])
def GetBookmarksbyid(request):
    data=request.data['user_id']
    data=ApplyBookmark.objects.filter(user_id=data)
    serializer=ApplyBookmarkSerializer(data,many=True)
    #print(serializer.data)
    l=[]
    for i in range(len(serializer.data[0]['item_id'])):
        print(serializer.data[0]['item_id'][i]['item_id'])
        l.append(serializer.data[0]['item_id'][i]['item_id'])
    data2=Apply.objects.filter(id__in=l)
    serializer2=ApplySerializer(data2,many=True)
    #print(serializer2.data)
    return Response({"status":200,"data":serializer2.data})
