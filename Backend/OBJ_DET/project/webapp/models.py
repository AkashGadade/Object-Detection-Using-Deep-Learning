from django.db import models

# Create your models here.
class ImageData(models.Model):
    imgname = models.CharField(max_length=100,null=True)
    img  = models.ImageField(upload_to='images/',max_length=300,null=True)
    