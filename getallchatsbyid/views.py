from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from chat.models import Message,Sender
from chat.serializers import MessageSerializer,ReceiverSerializer
# Create your views here.



@api_view(['POST'])
def GetallChats(request):
    data=request.data
    sender_data=Sender.objects.get(sender_userid=data['sender_userid'])
    #  .order_by("se__receiver").distinct()
    print(sender_data.se.order_by().values_list('receiver').distinct())
    # print(sender_data)

    # for i in sender_data:
        

        # print(i.se.values("receiver").distinct())
        # for j in i.se.values("receiver").distinct():
        #     print(type(j['receiver']))
        #     print(j)
        #     temp=ReceiverSerializer(j,many=True)
        #     print(temp.data)

    return Response({"status":200,"data":"Done"})



# @api_view(['POST'])
# def GetallChats(request):
#     data=request.data
#     obs=Sender.objects.filter(sender_userid=data['sender_userid'])
#     serializer=MessageSerializer(obs.se.all(),many=True)
#     print(serializer.data)
#     return Response({"status":200,"data":"Done"})

