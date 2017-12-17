from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
# from search.views import PostingFormView



urlpatterns = [
    # Examples:
    # url(r'^$','search.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls')),
    url(r'^search/$', 'search.views.search', name='search'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^search/', include('haystack.urls')),

]
