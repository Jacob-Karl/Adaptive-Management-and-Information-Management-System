from django.urls import re_path as url
from . import views


app_name='projects'
urlpatterns = [
    url(r'^$', views.hub, name='hub'),
    url(r'^Project/(?P<project_ID>\d+)/$', views.project, name='project'),
    url(r'^AddSpeCom/(?P<project_ID>\d+)/$', views.speComAdder, name='speComAdder'),
    url(r'^AddConMeas/(?P<project_ID>\d+)/$', views.conMeasAdder, name='conMeasAdder'),
    url(r'^AddLocation/(?P<project_ID>\d+)/$', views.locationAdder, name='locationAdder'),
    url(r'^AddGoal/(?P<project_ID>\d+)/$', views.goalAdder, name='goalAdder'),
    url(r'^RelatedProject/(?P<related_project_ID>\d+)/$', views.relatedProject, name='relatedProject'),
    url(r'^Trigger/(?P<trigger_ID>\d+)/$', views.trigger, name='trigger'),
    url(r'^TriggerStatus/(?P<trigger_status_ID>\d+)/$', views.triggerStatus, name='triggerStatus'),
    url(r'^Output/(?P<output_ID>\d+)/$', views.output, name='output'),
    url(r'^Objective/(?P<objective_ID>\d+)/$', views.objective, name='objective'),
    url(r'^Milestone/(?P<milestone_ID>\d+)/$', views.milestone, name='milestone'),
    url(r'^MilestoneProgress/(?P<milestone_progress_ID>\d+)/$', views.milestoneProgress, name='milestoneProgress'),
    url(r'^Step/(?P<step_ID>\d+)/$', views.step, name='step'),
    url(r'^Method/(?P<method_ID>\d+)/$', views.method, name='method'),
    url(r'^Protocol/(?P<protocol_ID>\d+)/$', views.protocol, name='protocol'),
    ]
