from django.shortcuts import render
from .models import Tango
from django.http import HttpResponse
from tango_with_django.models import Name


# Create your views here.
def index(request):
    return render(request,"home_template.html", {})

def home(request):
    name = request.GET.get("myname")
    #return HttpResponse(name)
    if name is not None or name  != '':
        Name.objects.create(name=name)        
    return HttpResponse("Your name has been saved to database! <a href='/users'> Click here to view you name </a>")

def users(request):    
    users = Name.objects.all()        
    return render(request,"home_template.html", {
    "users":users
    })
