from django.db import models
from django.utils import timezone


class Sender(models.Model):
    sender_userid=models.CharField(max_length=100)
    sender_name=models.CharField(max_length=50)
    sender_phone_number=models.CharField(max_length=50)
    sender_city=models.CharField(max_length=50)


    def __str__(self):
        return self.sender_userid

class Receiver(models.Model):
    receiver_userid=models.CharField(max_length=100)
    receiver_name=models.CharField(max_length=50)
    receiver_phone_number=models.CharField(max_length=50)
    receiver_city=models.CharField(max_length=50)

    def __str__(self):
        return self.receiver_userid

    


# Create your models here.
class Message(models.Model):
    sender=models.ForeignKey(Sender,on_delete=models.CASCADE,null=True,related_name='se')
    receiver=models.ForeignKey(Receiver,on_delete=models.CASCADE,null=True,related_name="re")
    message=models.CharField(max_length=1200)
    timestamp=models.DateTimeField(default=timezone.now)
    #is_read = models.BooleanField(default=False)
    def __str__(self):
        return self.message
    class Meta:
        ordering = ('timestamp',)
