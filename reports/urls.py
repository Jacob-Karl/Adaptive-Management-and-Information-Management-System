from django.conf.urls import url
from . import views


app_name='reports'
urlpatterns = [
    url(r'^$', views.hub, name='hub'),
    url(r'^generate_report/(?P<project_ID>\d+)/$', views.generate_report, name='generate_report'),
    ]
