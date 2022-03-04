from rest_framework import serializers
from .models import Sender,Receiver,Message


class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Sender
    
class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Receiver

class MessageSerializer(serializers.ModelSerializer):
    sender=SenderSerializer(read_only=True)
    receiver=ReceiverSerializer(read_only=True)
    class Meta:
        fields=("message",'sender','receiver')
        model=Message    