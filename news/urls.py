from django.conf.urls import url
from tango_with_django import views

urlpatterns = [
         
         url(r'^home$', views.home, name='home'),
         url(r'^$', views.index, name='index'),
]       