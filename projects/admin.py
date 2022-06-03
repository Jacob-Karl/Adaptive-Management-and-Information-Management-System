from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin
#@admin.register(Project)
class ClientModelAdmin(VersionAdmin):
    pass

# Register your models here.
@admin.register(Project)
class ProjectAdmin(VersionAdmin):
    pass

@admin.register(RelatedProject)
class RelatedProjectAdmin(VersionAdmin):
    pass

@admin.register(Trigger)
class TriggerAdmin(VersionAdmin):
    pass

@admin.register(TriggerStatus)
class TriggerStatusAdmin(VersionAdmin):
    pass

@admin.register(Output)
class OutputAdmin(VersionAdmin):
    pass

@admin.register(Objective)
class ObjectiveAdmin(VersionAdmin):
    pass

@admin.register(Milestone)
class MilestoneAdmin(VersionAdmin):
    pass

@admin.register(MilestoneProgress)
class MilestoneProgressAdmin(VersionAdmin):
    pass

@admin.register(Step)
class StepAdmin(VersionAdmin):
    pass

@admin.register(Protocol)
class ProtocolAdmin(VersionAdmin):
    pass