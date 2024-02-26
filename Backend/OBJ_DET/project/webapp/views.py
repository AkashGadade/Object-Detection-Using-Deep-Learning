from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ImageData


# Create your views here.
def Home(request):
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "upload":
            image = request.FILES.get('image')
            if image:
                insatance = ImageData.objects.create(img=image)

                return render(request , 'index.html' ,{'my_model': insatance})
            
            
    return render(request,"index.html")

