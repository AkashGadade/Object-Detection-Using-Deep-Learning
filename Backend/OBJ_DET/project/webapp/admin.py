from django.contrib import admin
from django.contrib.admin.sites import site
from .models import ImageData
# Register your models here.
class ImageDataAdmin(admin.ModelAdmin):
    list_display = ('id','img')
admin.site.register(ImageData,ImageDataAdmin)