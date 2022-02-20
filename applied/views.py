from pty import CHILD
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apply.models import Apply,ApplywithImages
from apply.serializers import ApplySerializer,ApplywithImagesSerializer
# Create your views here.

@api_view(['GET'])
def GetApplied(request):
    obs=Apply.objects.all().order_by('-created_date')
    # print(obs)
    # for i in obs:
    #     p=i.children.all()
    #     serializer2=ApplywithImagesSerializer(p,many=True)
        #print(serializer2.data)
    # obs2=ApplywithImages.objects.all()
    # print(obs)
    # for u in obs:
    #         #children.append(u.get_all_children())
    #     print(u.get_all_children())
    # print(list(obs))
    # obs2=ApplywithImages.objects.all()
    serializer=ApplySerializer(obs,many=True)
    #serializer2=ApplywithImagesSerializer(obs,many=True)
    return Response({"status":200,"data":serializer.data})
