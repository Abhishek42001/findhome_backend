from dataclasses import fields
from rest_framework import serializers
from .models import ApplyBookmark,Item_id

class ApplyBookmarkSerializer2(serializers.ModelSerializer):
    class Meta:
        model=Item_id
        fields=("item_id",)

class ApplyBookmarkSerializer(serializers.ModelSerializer):
    item_id=ApplyBookmarkSerializer2(many=True,read_only=True,source="ss")
    class Meta:
        model=ApplyBookmark
        exclude=("user_id","id")

    def create(self,validated_data):
        user_id=validated_data.getlist('user_id')
        item_id=validated_data.getlist('item_id')

        if ApplyBookmark.objects.filter(user_id=user_id[0]).exists():
            obj=ApplyBookmark.objects.get(user_id=user_id[0])
            instance=Item_id.objects.create(user_id_foriegn_key=obj,item_id=int(item_id[0]))
        else:
            obj=ApplyBookmark.objects.create(user_id=user_id[0])
            instance=Item_id.objects.create(user_id_foriegn_key=obj,item_id=int(item_id[0]))
        return instance
