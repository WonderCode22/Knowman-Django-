from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    #url(r'^$', views.search, name='index'),
    url(r'^case/(\d+)', views.case_details, name='case_details'),
    url(r'^tblinstallbase/$', views.search_tblinstallbase, name='tblinstallbase_search'),
    url(r'^tblinstallbase/(\d+)/$', views.tblescalation_by_case, name='tblescalation_search'),
    url(r'^searching/', 'search.views.searching', name='searching'),
    url(r'^pcomplete/', 'search.views.pcomplete', name='pcomplete'),
    url(r'^posting/', 'search.views.posting', name='posting'),
    url(r'^details/', 'search.views.case_details', name='details'),
]
