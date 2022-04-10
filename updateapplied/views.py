from django.shortcuts import render
from apply.models import Apply
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from apply.serializers import ApplySerializer
import cloudinary.uploader
# Create your views here.

#incomplete


@api_view(['POST'])
def updateCover(request):
    data=request.data
    try:
        #user id for security check, means no other user can update
        # print(data.get('user_id'))
        # print(data.get('database_id'))        
        # print(data.get('image'))
        # print(data.get("public_id"))
        print("Status:",cloudinary.uploader.upload(data.get('image'),public_id=data.get("public_id"),version=data.get('version'))),
        Apply.objects.filter(user_id=data.get('user_id'),id=data.get('database_id')).update(
            created_date=timezone.now()
        )
        return Response({"status":200,"message":"Success"})
    except Exception as e:
        print(e)
        return Response({"status":400,"message":e.args[0]})
    
@api_view(['POST'])
def updateOtherInfos(request):
    data=request.data
    try:
        Apply.objects.filter(user_id=data.get('user_id'),id=data.get('id')).update(
            owner_name=data.get("main_image"),
            title=data.get('title'),
            phone_number=data.get('phone_number'),
            address=data.get('address'),
            description=data.get('description'),
            price=data.get('price'),
            number_of_bathrooms=data.get('number_of_bathrooms'),
            number_of_bedrooms=data.get('number_of_bedrooms'),
            city=data.get('city'),
            type=data.get('type'),
            created_date=timezone.now()
        )
        return Response({"status":200,"message":"Success"})
    except Exception as e:
        return Response({"status":400,"message":e.args[0]})

@api_view(['POST'])
def updateAdditionalPhotos(request):
    data=request.data
    try:
        pass
    except Exception as e:
        return Response({"status":400,"message":e.args[0]})
 