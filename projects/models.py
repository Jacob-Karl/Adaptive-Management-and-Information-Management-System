import auto_prefetch
from django.db import models
from django import forms
from django.contrib.auth.models import User
#from user_functions.models import *
#from scopes.models import *


# Create your models here.

class Project(auto_prefetch.Model):
    STATUS_CHOICES = (
        ('Open','Open'),
        ('Closed','Closed'),
    )
    TYPE_CHOICES = (
        ('Fish Augmentation','Fish Augmentation'),
        ('Species Research','Species Research'),
        ('System Monitoring','System Monitoring'),
        ('Conservation Area Development and Management','Fish Augmentation'),
        ('Post-Development Monitoring','Post-Development Monitoring'),
        ('Adaptive Management Program','Adaptive Management Program'),
    )
    
    WorktaskID = models.CharField(max_length=10, default = "", null = True, db_index = True)
    ProjectName = models.CharField(max_length=255, default = "", null = True, db_index = True)
    ProjectLead = models.CharField(max_length=38, default = "", null = True, db_index = True)
    ProjectStatus = models.CharField(max_length=10, choices = STATUS_CHOICES, null = True, db_index = True)
    ProjectType = models.CharField(max_length=50, choices = TYPE_CHOICES, null = True, db_index = True)
    ProjectStart = models.DateField(null = True, db_index = True)
    ProjectEnd = models.DateField(null = True, db_index = True)
    ProjectSummary = models.TextField(default = "",null = True, db_index = True)
    ProjectBackground = models.TextField(default = "",null = True, db_index = True)
    OtherConsMeas = models.CharField(max_length=255, default = "",null = True, db_index = True)
    OtherSpecies = models.CharField(max_length=255, default = "",null = True, db_index = True)
    Reference = models.TextField(default = "", null=True, db_index = True)
    ProjectContributors = models.TextField(default = "", null = True, db_index = True)
    People = models.ManyToManyField('user_functions.Person')
    Goals = models.ManyToManyField('scopes.Goal', through='Goal2Project')
    SpeComs = models.ManyToManyField('scopes.SpeciesCommunity', through='SpeCom2Project')
    ConMeas = models.ManyToManyField('scopes.ConservationMeasure', through='ConMeas2Project')
    Locations = models.ManyToManyField('scopes.Location', through='Location2Project')
    Triggers = models.ManyToManyField('Trigger')
    Outputs = models.ManyToManyField('Output')
    Objectives = models.ManyToManyField('Objective')
    RelatedProjects = models.ManyToManyField('RelatedProject')
    
    def __str__(self):
        if self.WorktaskID is not None or self.WorktaskID is not '':
            return str(self.WorktaskID)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Projects"
        
    
    
class RelatedProject(auto_prefetch.Model):
    Project = auto_prefetch.ForeignKey(Project, on_delete=models.CASCADE)
    WorktaskID = models.CharField(default = "", max_length=10)
    RelationshipType = models.CharField(default = "", max_length=100)
    
    def __str__(self):
        if self.WorktaskID is not None:
            return str(self.WorktaskID)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Related Projects"    
    
class Trigger(auto_prefetch.Model):
    ProjectID = auto_prefetch.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
    TriggerName = models.CharField(max_length=38, default = "", null = True)
    TriggerDescription = models.TextField(default = "", null = True)
    TriggerIndicators = models.TextField(default = "", null = True)
    ProposedResponse = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    TriggerStatus = models.ManyToManyField('TriggerStatus')
    
    def __str__(self):
        if self.TriggerName is not None:
            return str(self.TriggerName)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Triggers"    

class TriggerStatus(auto_prefetch.Model):
    TriggerID = auto_prefetch.ForeignKey(Trigger, on_delete=models.CASCADE)
    ReportingDate = models.DateField(null = True)
    StatusTrend = models.TextField(default = "", null = True)
    MgmtInterp = models.TextField(default = "", null = True)
    MgmtResponse = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    
    def __str__(self):
        if self.TriggerID.TriggerName != '' or self.TriggerID.TriggerName is not None:
            return str(self.TriggerID.TriggerName)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Trigger Statuses"    

class Output(auto_prefetch.Model):
    ProjectID = auto_prefetch.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
    OutputType = models.CharField(max_length=100, default = "", null = True)
    OutputAuthors = models.CharField(max_length=255, default = "", null = True)
    OutputDate = models.DateField(null = True)
    OutputTitle = models.TextField(max_length=226, default = "", null = True)
    OutputVersion = models.CharField(max_length=10, default = "", null = True)
    OutputDescription = models.TextField(default = "", null = True)
    OutputDOI = models.CharField(max_length=100, default = "", null = True)
    OutputCitation = models.TextField(default = "", null = True)
    OutputURI = models.CharField(max_length=255, default = "", null = True)
    OutputConstraints = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    
    def __str__(self):
        if self.OutputTitle != '' or self.OutputTitle is not None:
            return str(self.OutputTitle)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Outputs"    

class Objective(auto_prefetch.Model):
    ProjectID = auto_prefetch.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
    ObjCode = models.CharField(max_length=25, default = "", null = True)
    ObjName = models.CharField(max_length=100, default = "", null = True)
    ObjDescription = models.TextField(default = "", null = True)
    ObjStartDate = models.DateField(null = True)
    ObjEndDate = models.DateField(null = True)
    ObjFlowDiagram = models.CharField(max_length=255, default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    Milestones = models.ManyToManyField('Milestone')
    Steps = models.ManyToManyField('Step', through='Objective2Step')
    
    def __str__(self):
        if self.ObjCode != '' or self.ObjCode is not None:
            return str(self.ObjCode)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Objectives"    

class Milestone(auto_prefetch.Model):
    ObjectiveID = auto_prefetch.ForeignKey(Objective, on_delete=models.CASCADE)
    MilestoneID = models.CharField(max_length=25, default = "", null = True)
    MilestoneName = models.CharField(max_length=100, default = "", null = True)
    Description = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    MilestoneProgress = models.ManyToManyField('MilestoneProgress')
    
    def __str__(self):
        if self.MilestoneID != '' or self.MilestoneID is not None:
            return str(self.MilestoneID)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Milestones"    

class MilestoneProgress(auto_prefetch.Model):
    MilestoneID = auto_prefetch.ForeignKey(Milestone, on_delete=models.CASCADE)
    ReportingDate = models.DateField(null = True)
    Status = models.CharField(max_length=25, default = "", null = True)
    Description = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    
    def __str__(self):
        if self.MilestoneID.MilestoneID != '' or self.MilestoneID.MilestoneID is not None:
            return str(self.MilestoneID.MilestoneID)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Milestone Progresses"    

class Step(auto_prefetch.Model):
    ObjectiveID = auto_prefetch.ForeignKey(Objective, on_delete=models.CASCADE)
    StepName = models.CharField(max_length=100, default = "", null = True)
    StepCode = models.CharField(max_length=10, default = "", null = True)
    StepType = models.CharField(max_length=100, default = "", null = True)
    StepSummary = models.TextField(default = "", null = True)
    StepStartDate = models.DateField(null = True)
    StepEndDate = models.DateField(null = True)
    StepDependencies = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    Methods = models.ManyToManyField('Method', through='Step2Method')
    
    def __str__(self):
        if self.StepCode != '' or self.StepCode is not None:
            return str(self.StepCode)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Steps"    

class Method(auto_prefetch.Model):
    StepID = auto_prefetch.ForeignKey(Step, on_delete=models.CASCADE)
    MethodTitle = models.CharField(max_length=255, default = "", null = True)
    MethodCode = models.CharField(max_length=10, default = "", null = True)
    MethodType = models.CharField(max_length=50, default = "", null = True)
    MethodDate = models.DateField(null = True)
    MethodVersion = models.CharField(max_length=10, default = "", null = True)
    MethodDescription = models.TextField(default = "", null = True)
    MethodContact = models.CharField(max_length=38, default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    Protocols = models.ManyToManyField('Protocol', through='Method2Protocol')
    
    def __str__(self):
        if self.MethodCode != '' or self.MethodCode is not None:
            return str(self.MethodCode)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Methods"    

class Protocol(auto_prefetch.Model):
    MethodID = auto_prefetch.ForeignKey(Method, on_delete=models.CASCADE)
    ProtocolCode = models.CharField(max_length=10, default = "", null = True)
    ProtocolTitle = models.CharField(max_length=255, default = "", null = True)
    ProtocolVerision = models.CharField(max_length=10, default = "", null = True)
    ProtocolDate = models.DateField(null = True)
    ProtocolAuthor = models.CharField(max_length=255, default = "", null = True)
    ProtocolDescription = models.TextField(default = "", null = True)
    ProtocolLink = models.CharField(max_length=255, default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    
    def __str__(self):
        if self.ProtocolCode != '' or self.ProtocolCode is not None:
            return str(self.ProtocolCode)
        else:
            return 'None'
    
    class Meta(auto_prefetch.Model.Meta):
        verbose_name_plural = "Protocols"    

#Linking Models

class SpeCom2Project(models.Model):
    SpeComID = models.ForeignKey('scopes.SpeciesCommunity', on_delete=models.CASCADE)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)

class Location2Project(models.Model):
    LocationID = models.ForeignKey('scopes.Location', on_delete=models.CASCADE)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)

class ConMeas2Project(models.Model):
    ConMeasID = models.ForeignKey('scopes.ConservationMeasure', on_delete=models.CASCADE)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)

class Goal2Project(models.Model):
    GoalID = models.ForeignKey('scopes.Goal', on_delete=models.CASCADE)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)

class Project2Output(models.Model):
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)
    OutputID = models.ForeignKey(Output, on_delete=models.CASCADE)

class Objective2Step(models.Model):
    ObjectiveID = models.ForeignKey(Objective, on_delete=models.CASCADE)
    StepID = models.ForeignKey(Step, on_delete=models.CASCADE)
    
class Step2Method(models.Model):
    StepID = models.ForeignKey(Step, on_delete=models.CASCADE)
    MethodID = models.ForeignKey(Method, on_delete=models.CASCADE)

class Method2Protocol(models.Model):
    MethodID = models.ForeignKey(Method, on_delete=models.CASCADE)
    ProtocolID = models.ForeignKey(Protocol, on_delete=models.CASCADE)