from rest_framework import serializers
from .models import Apply,ApplywithImages

class ApplywithImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ApplywithImages
        fields=("images",)
    

class ApplySerializer(serializers.ModelSerializer):
    images =ApplywithImagesSerializer(many=True,source="tt",read_only=True)
    class Meta:
        model=Apply
        exclude=("user_id",)
    
    def create(self, validated_data):
        images = validated_data.getlist('images')
        print("images:",images)
        
        obj = Apply.objects.create(
            user_id=validated_data.get('user_id'),
            owner_name=validated_data.get("owner_name"),
            title=validated_data.get("title"),
            phone_number=validated_data.get("phone_number"),
            address=validated_data.get("address"),
            description=validated_data.get("description"),
            price=validated_data.get("price"),
            number_of_bathrooms=validated_data.get("number_of_bathrooms"),
            number_of_bedrooms=validated_data.get("number_of_bedrooms"),
            city=validated_data.get("city"),
            main_image=validated_data.get("main_image"),
            type=validated_data.get("type"),
            profile_pic_url=validated_data.get("profile_pic_url"),
        )
        for image_data in images:
        	ApplywithImages.objects.create(user_details=obj, images=image_data)
