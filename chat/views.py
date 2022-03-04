from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import MessageSerializer
from rest_framework.response import Response
from .models import Message,Sender,Receiver
# Create your views here.


@api_view(['POST'])
def sendmessage(request):
    data=request.data
    print(data)
    #serializer=MessageSerializer(data=data)
    #print(serializer)
    #if serializer.is_valid():
    try:
        if not Sender.objects.filter(sender_userid=request.data['sender_userid']).exists():
            sender=Sender.objects.create(
                sender_name=request.data['sender_name'],
                sender_userid=request.data['sender_userid'],
                sender_phone_number=request.data['sender_phone_number'],
                sender_city=request.data['sender_city']
            )
        else:
            sender=Sender.objects.get(sender_userid=request.data['sender_userid'])
        if not Receiver.objects.filter(receiver_userid=request.data['receiver_userid']).exists():
            receiver=Receiver.objects.create(
                receiver_name=request.data['receiver_name'],
                receiver_userid=request.data['receiver_userid'],
                receiver_phone_number=request.data['receiver_phone_number'],
                receiver_city=request.data['receiver_city']
            )
        else:
            receiver=Receiver.objects.get(receiver_userid=request.data['receiver_userid'])
        Message.objects.create(sender=sender,receiver=receiver,message=request.data['message'])
        return Response({"status": 200,"message":"Success"})
    except Exception as e:
        
        return Response({"status":400,"message":e.args[0]+" Missing..."})
    
    # return Response({"status":400,"message":serializer.errors})