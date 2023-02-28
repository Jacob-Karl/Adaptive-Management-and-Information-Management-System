from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin

#@admin.register(Project)
class ClientModelAdmin(VersionAdmin):
    pass

# Register your models here.
@admin.register(Project)
class ProjectAdmin(VersionAdmin): 
    list_select_related = True    
    
    list_field = (
        'WorktaskID',
        'ProjectName',
    )
    
    list_filter = (
        'WorktaskID',
        'ProjectName',
    )
    
    search_fields = [
        'WorktaskID',
        'ProjectName',
        'ProjectLead',
        'ProjectStatus',
        'ProjectType',
        'ProjectStart',
        'ProjectEnd',
        'ProjectSummary',
        'ProjectBackground',
        'OtherConsMeas',
        'OtherSpecies',
        'Reference',
        'ProjectContributors',
        
        'People__LastName',
        'People__FirstName',
        
        'Goals__GoalName',
        'SpeComs__Acronym',
        'ConMeas__CMCode',
        'Locations__LocationCode',
        #]
        'Triggers__TriggerName',
        'Outputs__OutputTitle',
        'Objectives__ObjCode',
        
        'Objectives__ObjName',
        'RelatedProjects__WorktaskID',
        ]

@admin.register(RelatedProject)
class RelatedProjectAdmin(VersionAdmin):
    search_fields = [
        'Project__WorktaskID',
        'Project__ProjectName',
        'WorktaskID',
        'RelationshipType',
    ]

@admin.register(Trigger)
class TriggerAdmin(VersionAdmin):
    search_fields = [
        'ProjectID__WorktaskID',
        'ProjectID__ProjectName',        
        'TriggerName',
        'TriggerDescription',
        'TriggerIndicators',
        'ProposedResponse',
        'Reference',
        'TriggerStatus__StatusTrend',
    ]

@admin.register(TriggerStatus)
class TriggerStatusAdmin(VersionAdmin):
    search_fields = [
        'TriggerID__TriggerName',
        'ReportingDate',
        'StatusTrend',
        'MgmtInterp',
        'MgmtResponse',
        'Reference',
    ]

@admin.register(Output)
class OutputAdmin(VersionAdmin):
    search_fields = [
        'ProjectID__WorktaskID',
        'ProjectID__ProjectName',
        'OutputType',
        'OutputAuthors',
        'OutputDate',
        'OutputTitle',
        'OutputVersion',
        'OutputDescription',
        'OutputDOI',
        'OutputCitation',
        'OutputURI',
        'OutputConstraints',
        'Reference',
    ]

@admin.register(Objective)
class ObjectiveAdmin(VersionAdmin):
    search_fields = [
        'ProjectID__WorktaskID',
        'ProjectID__ProjectName',
        'ObjCode',
        'ObjName',
        'ObjDescription',
        'ObjStartDate',
        'ObjEndDate',
        'ObjFlowDiagram',
        'Reference',
        'Milestones__MilestoneID',
        'Milestones__MilestoneName',
        'Steps__StepName',
        'Steps__StepCode',
    ]

@admin.register(Milestone)
class MilestoneAdmin(VersionAdmin):
    search_fields = [
        'ObjectiveID__ObjCode',
        'ObjectiveID__ObjName',
        'MilestoneID',
        'MilestoneName',
        'Description',
        'Reference',
        'MilestoneProgress__Status',
        'MilestoneProgress__Description',
    ]

@admin.register(MilestoneProgress)
class MilestoneProgressAdmin(VersionAdmin):
    search_fields = [
        'MilestoneID__MilestoneID',
        'MilestoneID__MilestoneName',
        'ReportingDate',
        'Status',
        'Description',
        'Reference',
    ]

@admin.register(Step)
class StepAdmin(VersionAdmin):
    search_fields = [
        'ObjectiveID__ObjCode',
        'ObjectiveID__ObjName',
        'StepName',
        'StepCode',
        'StepType',
        'StepSummary',
        'StepStartDate',
        'StepEndDate',
        'StepDependencies',
        'Reference',     
        'Methods__MethodTitle',
        'Methods__MethodCode', 
    ]

@admin.register(Method)
class MethodAdmin(VersionAdmin):
    search_fields = [
        'StepID__StepName',
        'StepID__StepCode',
        'MethodTitle',
        'MethodCode',
        'MethodType',
        'MethodDate',
        'MethodVersion',
        'MethodDescription',
        'MethodContact',
        'Reference',
        'Protocols__ProtocolCode',
        'Protocols__ProtocolTitle',
    ]

@admin.register(Protocol)
class ProtocolAdmin(VersionAdmin):
    search_fields = [
        'MethodID__MethodTitle',
        'MethodID__MethodCode',
        'ProtocolCode',
        'ProtocolTitle',
        'ProtocolVerision',
        'ProtocolDate',
        'ProtocolAuthor',
        'ProtocolDescription',
        'ProtocolLink',
        'Reference',
    ]