from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='index'),
    url(r'^case/(\d+)', views.case_details, name='case_details'),
]