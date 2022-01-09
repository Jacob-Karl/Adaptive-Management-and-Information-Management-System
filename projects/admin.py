from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(RelatedProject)
admin.site.register(Trigger)
admin.site.register(TriggerStatus)
admin.site.register(Output)
admin.site.register(Objective)
admin.site.register(Milestone)
admin.site.register(MilestoneProgress)
admin.site.register(Step)
admin.site.register(Method)
admin.site.register(Protocol)