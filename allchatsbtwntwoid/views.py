from django.shortcuts import render
from chat.models import Message
from rest_framework.response import Response
from rest_framework.decorators import api_view
from chat.serializers import MessageSerializer
from django.db.models import Q
# Create your views here.

#sender__sender_userid     sender is foriegn key name and sender_userid is field name of that foriegn key

@api_view(['POST'])
def Getallchatsbtwntwo(request):
    data=request.data
    try:
        message_data=Message.objects.filter(Q(sender__sender_userid=data['sender_userid'],receiver__receiver_userid=data['receiver_userid'])|\
            Q(sender__sender_userid=data['receiver_userid'],receiver__receiver_userid=data['sender_userid'])).order_by('-timestamp')
        messages=[]
        for i in message_data:
            serializer=MessageSerializer(i)
            messages.append(serializer.data)
        return Response({"status":200,"message":messages})
    except Exception as e:
        return Response({"status":200,"message":e.args[0]})