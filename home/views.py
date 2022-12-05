from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
def contact(request):
    messages.error(request, 'welcome to contact')
    if request.method=='POST':
        #print('we are using post request')
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name,email,phone,content)
        if len(name)<4:
            messages.error("error text")
        else:    
         contact=Contact(name=name,email=email,phone=phone,content=content)
         contact.save()
         messages.success(request,"successful")

    return render(request,'home/contact.html') 
