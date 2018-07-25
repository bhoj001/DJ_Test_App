from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from forms_example.views import review_input

def home(request):     
    form={}
    form["review_input"]=review_input
    return render(request,"index.html", {"form" :form })

