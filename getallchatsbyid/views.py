from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from chat.models import Message,Sender,Receiver
from chat.serializers import MessageSerializer,ReceiverSerializer
from dateutil.parser import *
# Create your views here.



@api_view(['POST'])
def GetallChats(request):
    data=request.data
    try:
        response_list=[]
        

        #looking for received data
        Receiver_data=Receiver.objects.get(receiver_userid=data['sender_userid'])
        Receiver_data=Receiver_data.re.order_by('-sender_id','timestamp').distinct('sender')

        #looking for sent data
        sender_data=Sender.objects.get(sender_userid=data['sender_userid'])
        sender_data=sender_data.se.order_by('-receiver_id','timestamp').distinct('receiver')

        d1=MessageSerializer(Receiver_data[0]).data['timestamp']
        d2=MessageSerializer(sender_data[0]).data['timestamp']

        #print(parse(d1)>parse(d2))

        #print(Receiver_data)
        if parse(d1)>parse(d2):
            for i in Receiver_data:
                serializer=MessageSerializer(i)
                response_list.append(serializer.data)
            for i in sender_data:
                serializer=MessageSerializer(i)
                response_list.append(serializer.data)
        else:
            for i in sender_data:
                serializer=MessageSerializer(i)
                response_list.append(serializer.data)
            for i in Receiver_data:
                serializer=MessageSerializer(i)
                response_list.append(serializer.data)
        return Response({"status":200,"data":response_list})
    except Exception as e:
        print(e)
        return Response({"status":200,"data":e.args[0]})


# @api_view(['POST'])
# def GetallChats(request):
#     data=request.data
#     obs=Sender.objects.filter(sender_userid=data['sender_userid'])
#     serializer=MessageSerializer(obs.se.all(),many=True)
#     print(serializer.data)
#     return Response({"status":200,"data":"Done"})

