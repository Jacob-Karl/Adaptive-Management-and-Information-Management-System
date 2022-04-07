from django.conf.urls import url
from . import views


app_name='user_functions'
urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^hub/$', views.hub, name='hub'),
    url(r'^settings/(?P<user_id>\d+)/$', views.settings, name='settings'),
    ]
