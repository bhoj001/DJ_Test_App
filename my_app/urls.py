"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views 
from tango_with_django.views import home as tango_home
from tango_with_django.views import users
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home, name='tango' ),
    # url(r'^tango_with_django/', include('tango_with_django.urls',namespace="tango_with_django")),
    #  url(r'^mydata/$', tango_home ),
    #  url(r'^users/$', users ),
    #  url(r'^news/$',include('news.urls',namespace="news")),
    #  url(r'^forms_classbased_views_app/$',include('forms_classbased_views_app.urls')),
    url(r'^$', include('ElasticSearchExample.urls',namespace="ElasticSearchExample")),
    url(r'^formset/', include('formset_example.urls',namespace="formset_example")),

]
