from dataclasses import fields
from rest_framework import serializers
from .models import ApplyBookmark

class ApplyBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApplyBookmark
        fields="__all__"