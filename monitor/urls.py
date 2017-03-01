"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from monitor import views

urlpatterns = [
    url(r'^netusage/?$', views.net_usage),
    url(r'^netusage/(?P<interface>\w*)/?$', views.net_usage),
    url(r'^netusage/(?P<interface>\w*)/'
        r'(?P<traffic_set>days|tops|months|hours)/?$', views.net_usage),
    url(r'^netusage/(?P<interface>\w*)/(?P<traffic_set>days|tops|months|hours)/'
        r'(?P<from_date>\d{1,4}-\d{1,2}-\d{1,2})/?$', views.net_usage),
    url(r'^netusage/(?P<interface>\w*)/(?P<traffic_set>days|tops|months|hours)/'
        r'(?P<from_date>\d{1,4}-\d{1,2}-\d{1,2})/'
        r'(?P<to_date>\d{1,4}-\d{1,2}-\d{1,2})/?$', views.net_usage)
]
