from django.conf.urls import url, include
from . import views

# Application level namespace.
app_name = "formset_example"

urlpatterns = [
    # url(r'^$', views.formset, name="formset"),

    # /documents/<document_id>
    url(r'^$', views.FormsetView.as_view(), name="formset"),
]
