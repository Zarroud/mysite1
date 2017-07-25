from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib import admin


urlpatterns = [
url(r'^$', views.login, name="login"),
    url(r'^monitorUsers/$', views.monitorUsers, name='monitorUsers'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^auth/$', views.auth_view, name="auth"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^loggedin/$', views.loggedin, name="loggedin"),
    url(r'^invalid/$', views.invalid, name="invalid"),
	url(r'^(?P<pk>\d+)/del_user/$', views.del_user, name="delete"),
	url(r'^(?P<pk>\d+)/activate_user/$', views.activate_user, name="activate_user"),
	url(r'^(?P<pk>\d+)/desactivate_user/$', views.desactivate_user, name="desactivate_user"),
	url(r'^find_user/$', views.find_user, name="find_user"),
	url(r'^listEmailConf/$', views.listEmailConf, name="listEmailConf"),
	url(r'^contact/$', views.contact, name="contact"),
	url(r'^contactBymail/$', views.contactBymail, name="contactBymail"),
]
