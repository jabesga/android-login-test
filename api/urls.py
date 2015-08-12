from django.conf.urls import patterns, url
from api import views

from rest_framework.authtoken import views as authtoken

urlpatterns = patterns('',
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', authtoken.obtain_auth_token),
                       url(r'^access/$', views.access, name='access'),
                       )