from django.conf.urls import patterns, url
from quickstart import views


urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       )