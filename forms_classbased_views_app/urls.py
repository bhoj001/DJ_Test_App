from . import views
from django.conf.urls import url

urlpatterns = [
    
    # we're using a class-based view here!
    url(r'^about-us/$', views.AboutUsView.as_view(), name='about_us'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
]


