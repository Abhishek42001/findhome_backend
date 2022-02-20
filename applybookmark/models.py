from django.db import models

# Create your models here.
class ApplyBookmark(models.Model):
    user_id=models.CharField(max_length=100)
    owner_name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.IntegerField()
    number_of_bathrooms=models.IntegerField()
    number_of_bedrooms=models.IntegerField()
    city=models.CharField(max_length=50)
