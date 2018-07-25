from django.conf.urls import url
from . import views

# Application level namespace.
#app_name = "review_system"

urlpatterns = [
    # /review_system/
    url(r'^$', views.review_input, name="review_system"),

   ]
