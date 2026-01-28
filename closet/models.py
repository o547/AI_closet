from django.db import models
import uuid
# Create your models here.
class garment(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,verbose_name="ID")
    name=models.CharField(max_length=100,verbose_name="名前")
    color=models.CharField(max_length=100,verbose_name="色")
    type=models.CharField(max_length=100,default="未指定",verbose_name="分類")
    cleated=models.DateField(auto_now_add=True,verbose_name="作成日時")

    def __str__(self):
        return self.name
    
class coordinate(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,verbose_name="ID")
    temperature=models.CharField(max_length=100,null=True,verbose_name="気温設定")
    tops=models.CharField(max_length=100,null=True,verbose_name="トップス")
    bottoms=models.CharField(max_length=100,null=True,verbose_name="ボトムス")
    outer=models.CharField(max_length=100,null=True,verbose_name="アウター")
    inner=models.CharField(max_length=100,null=True,verbose_name="インナー")
    accessory=models.CharField(max_length=100,null=True,verbose_name="アクセサリー")
    additional1=models.CharField(max_length=100,null=True,verbose_name="追加１")
    additional2=models.CharField(max_length=100,null=True,verbose_name="追加２")
    cleated=models.DateField(auto_now_add=True,verbose_name="作成日時")
    def __str__(self):
        return str(self.id)