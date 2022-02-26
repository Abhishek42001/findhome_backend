from django.db import models

# Create your models here.
class ApplyBookmark(models.Model):
    user_id=models.CharField(max_length=150)

class Item_id(models.Model):
    user_id_foriegn_key=models.ForeignKey(ApplyBookmark,on_delete=models.CASCADE,related_name="ss",)
    item_id=models.IntegerField()