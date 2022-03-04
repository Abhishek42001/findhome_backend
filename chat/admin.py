from django.contrib import admin
from .models import Message,Sender,Receiver
# Register your models here.

admin.site.register(Message)

admin.site.register(Sender)

admin.site.register(Receiver)