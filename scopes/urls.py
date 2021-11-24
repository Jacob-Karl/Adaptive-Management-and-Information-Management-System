from django.conf.urls import url
from . import views


app_name='scopes'
urlpatterns = [
    url(r'^$', views.hub, name='hub'),
    url(r'^SpeCom/(?P<speCom_ID>\d+)/$', views.speCom, name='speCom'),
    url(r'^Location/(?P<loc_ID>\d+)/$', views.location, name='location'),
    url(r'^ConMeasure/(?P<conMea_ID>\d+)/$', views.conMeasure, name='conMeasure'),
    url(r'^Goal/(?P<goal_ID>\d+)/$', views.goal, name='goal'),
    ]
