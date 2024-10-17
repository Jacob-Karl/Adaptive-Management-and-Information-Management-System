from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin
from advanced_filters.admin import AdminAdvancedFiltersMixin

#@admin.register(Project)
class ClientModelAdmin(CompareVersionAdmin):
    pass

# Register your models here.
@admin.register(Project)
class ProjectAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin): 
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
    
    advanced_filter_fields = (
        ('WorktaskID', 'Worktask ID'),
        ('ProjectName', 'Project Name'),
        ('ProjectLead', 'Project Lead'),
        ('ProjectStatus', 'Project Status'),
        ('ProjectType', ' Project Type'),
        ('ProjectStart', 'Project Start Date'),
        ('ProjectEnd', 'Project End Date'),
        ('ProjectSummary', 'Project Summary'),
        ('ProjectBackground', 'Project Background'),
        ('OtherConsMeas', 'Other Conservation Measures'),
        ('OtherSpecies', 'Other Species'),
        ('Reference', 'Raference'),
        ('ProjectContributors', 'Project Contributors'),
        
        ('People__LastName', 'Last Name'),
        ('People__FirstName', 'First Name'),
        
        ('Goals__GoalName', 'Goal Name'),
        ('SpeComs__Acronym', 'Species/Community Acronym'),
        ('ConMeas__CMCode', 'Conservation Measure Code'),
        ('Locations__LocationCode', 'Location Code'),
        
        ('Triggers__TriggerName', 'Trigger Name'),
        ('Outputs__OutputTitle', 'Objective Title'),
        ('Objectives__ObjCode', 'Objective Code'),
        
        ('Objectives__ObjName', 'Objective Name'),
        ('RelatedProjects__WorktaskID', 'Related Project ID'),            
    )

@admin.register(RelatedProject)
class RelatedProjectAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
    search_fields = [
        'Project__WorktaskID',
        'Project__ProjectName',
        'WorktaskID',
        'RelationshipType',
    ]
    advanced_filter_fields = (
        ('Project__WorktaskID',' Parent Worktask ID'),
        ('Project__ProjectName','Parent Project Name'),
        ('WorktaskID','Worktask ID'),
        ('RelationshipType','Relationship Type'),
        )

@admin.register(Trigger)
class TriggerAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
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
    advanced_filter_fields = (
        ('ProjectID__WorktaskID','Worktask ID'),
        ('ProjectID__ProjectName','ProjectName'),
        ('TriggerName','Trigger Name'),
        ('TriggerDescription', 'Trigger Description'),
        ('TriggerIndicators', 'Trigger Indicators'),
        ('ProposedResponse', 'Proposed Response'),
        ('Reference', 'Reference'),
        ('TriggerStatus__StatusTrend', 'Trigger Status Trend'),
        )

@admin.register(TriggerStatus)
class TriggerStatusAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
    search_fields = [
        'TriggerID__TriggerName',
        'ReportingDate',
        'StatusTrend',
        'MgmtInterp',
        'MgmtResponse',
        'Reference',
    ]
    advanced_filter_fields = (
        ('TriggerID__TriggerName', 'Trigger Name'),
        ('ReportingDate', 'Reporting Date'),
        ('StatusTrend', 'Status Trend'),
        ('MgmtInterp', 'Management Interpretation'),
        ('MgmtResponse', 'Management Response'),
        ('Reference', 'Reference'),
        )

@admin.register(Output)
class OutputAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
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
    advanced_filter_fields = (
        ('ProjectID__WorktaskID', 'Worktask ID'),
        ('ProjectID__ProjectName', 'Project Name'),
        ('OutputType', 'Output Type'),
        ('OutputAuthors', 'Output Authors'),
        ('OutputDate', 'Output Date'),
        ('OutputTitle', 'Output Title'),
        ('OutputVersion', 'Output Version'),
        ('OutputDescription', 'Output Description'),
        ('OutputDOI', 'Output DOI'),
        ('OutputCitation', 'Output Citation'),
        ('OutputURI', 'Output URI'),
        ('OutputConstraints', 'Output Constraints'),
        ('Reference', 'Reference'),
        )

@admin.register(Objective)
class ObjectiveAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
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
    advanced_filter_fields = (
        ('ProjectID__WorktaskID', 'Worktask ID'),
        ('ProjectID__ProjectName', 'Project Name'),
        ('ObjCode', 'Objective Code'),
        ('ObjName', 'Objective Name'),
        ('ObjDescription', 'Objective Description'),
        ('ObjStartDate', 'Objective Start Date'),
        ('ObjEndDate', 'Objective End Date'),
        ('ObjFlowDiagram', 'Objective Flow Diagram'),
        ('Reference', 'Reference'),
        ('Milestones__MilestoneID', 'Milestone ID'),
        ('Milestones__MilestoneName', 'Milestone Name'),
        ('Steps__StepName', 'Step Name'),
        ('Steps__StepCode', 'Step Code'),
        )

@admin.register(Milestone)
class MilestoneAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
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
    advanced_filter_fields = (
        ('ObjectiveID__ObjCode', 'Objective Code'),
        ('ObjectiveID__ObjName', 'Objective Name'),
        ('MilestoneID', 'Milestone ID'),
        ('MilestoneName', 'Milestone Name'),
        ('Description', 'Description'),
        ('Reference', 'Reference'),
        ('MilestoneProgress__Status', 'Milestone Progress Status'),
        ('MilestoneProgress__Description', 'Milestone Progress Description'),
        )


@admin.register(MilestoneProgress)
class MilestoneProgressAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
    search_fields = [
        'MilestoneID__MilestoneID',
        'MilestoneID__MilestoneName',
        'ReportingDate',
        'Status',
        'Description',
        'Reference',
    ]
    advanced_filter_fields = (
        ('MilestoneID__MilestoneID', 'Milestone ID'),
        ('MilestoneID__MilestoneName', 'Milestone Name'),
        ('ReportingDate', 'Reporting Date'),
        ('Status', 'Status'),
        ('Description', 'Description'),
        ('Reference', 'Reference'),
        )

@admin.register(Step)
class StepAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
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
    advanced_filter_fields = (
        ('ObjectiveID__ObjCode', 'Objective Code'),
        ('ObjectiveID__ObjName', 'Objective Name'),
        ('StepName', 'Step Name'),
        ('StepCode', 'Step Code'),
        ('StepType', 'Step Type'),
        ('StepSummary', 'Step Summary'),
        ('StepStartDate', 'Step Start Date'),
        ('StepEndDate', 'Step End Date'),
        ('StepDependencies', 'Step Dependencies'),
        ('Reference', 'Reference'),
        ('Methods__MethodTitle', 'Method Title'),
        ('Methods__MethodCode', 'Method Code'),
        )

@admin.register(Method)
class MethodAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
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
    advanced_filter_fields = (
        ('StepID__StepName', 'Step Name'),
        ('StepID__StepCode', 'Step Code'),
        ('MethodTitle', 'Method Title'),
        ('MethodCode', 'Method Code'),
        ('MethodType', 'Method Type'),
        ('MethodDate', 'Method Date'),
        ('MethodVersion', 'Method Version'),
        ('MethodDescription', 'Method Description'),
        ('MethodContact', 'Method Contact'),
        ('Reference', 'Reference'),
        ('Protocols__ProtocolCode', 'Protocol Code'),
        ('Protocols__ProtocolTitle', 'Protocol Title'),
        )

@admin.register(Protocol)
class ProtocolAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
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
    advanced_filter_fields = (
        ('MethodID__MethodTitle', 'Method Title'),
        ('MethodID__MethodCode', 'Method Code'),
        ('ProtocolCode', 'Protocol Code'),
        ('ProtocolTitle', 'Protocol Title'),
        ('ProtocolVerision', 'Protocol Verision'),
        ('ProtocolDate', 'Protocol Date'),
        ('ProtocolAuthor', 'Protocol Author'),
        ('ProtocolDescription', 'Protocol Description'),
        ('ProtocolLink', 'Protocol Link'),
        ('Reference', 'Reference'),
        )