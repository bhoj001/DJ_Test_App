from django.conf.urls import url
from tango_with_django import views

urlpatterns = [
         url(r'^', views.index, name='index'),
        url(r'^index$', views.index, name='index'),
]