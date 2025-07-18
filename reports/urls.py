from django.conf.urls import url
from . import views


app_name='reports'
urlpatterns = [
    url(r'^$', views.hub, name='hub'),
    url(r'^report/(?P<project_ID>\d+)/$', views.prepare_report, name='report'),
    url(r'^generate_report/(?P<project_ID>\d+)/$', views.generate_report, name='generate_report'),
    url(r'^generate_project_report/(?P<project_ID>\d+)/$', views.generate_project_report, name='generate_project_report'),
    ]
