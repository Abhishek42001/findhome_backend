from django.db import models

import datetime
import os
from django.utils import timezone
# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Apply(models.Model):
    user_id=models.CharField(max_length=100)
    owner_name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=12)
    address=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.IntegerField()
    number_of_bathrooms=models.IntegerField()
    number_of_bedrooms=models.IntegerField()
    city=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    main_image=models.ImageField()
    created_date=models.DateTimeField('date created',default=timezone.now)
    profile_pic_url=models.CharField(max_length=1000)

class ApplywithImages(models.Model):
    user_details=models.ForeignKey(Apply,on_delete=models.CASCADE,related_name="tt")
    images=models.ImageField()

# {
#     "id":11,
#     "owner_name":"Abhishek",
#     "title":"Abhi",
#     "phone_number":123456789,
#     "city":"Dtg",
#     "address":"Address",
#     "description":"dsfsf",
#     "price":1222,
#     "number_of_bathrooms":11,
#     "number_of_bedrooms":11
# }
