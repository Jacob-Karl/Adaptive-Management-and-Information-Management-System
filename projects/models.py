from django.db import models
from django import forms
from django.contrib.auth.models import User
#from user_functions.models import *
#from scopes.models import *


# Create your models here.

class Project(models.Model):
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
    
    WorktaskID = models.CharField(max_length=10, default = "", null = True)
    ProjectName = models.CharField(max_length=255, default = "", null = True)
    ProjectLead = models.CharField(max_length=38, default = "", null = True)
    ProjectStatus = models.CharField(max_length=10, choices = STATUS_CHOICES, null = True)
    ProjectType = models.CharField(max_length=50, choices = TYPE_CHOICES, null = True)
    ProjectStart = models.DateField(null = True)
    ProjectEnd = models.DateField(null = True)
    ProjectSummary = models.TextField(default = "",null = True)
    ProjectBackground = models.TextField(default = "",null = True)
    OtherConsMeas = models.CharField(max_length=255, default = "",null = True)
    OtherSpecies = models.CharField(max_length=255, default = "",null = True)
    Reference = models.TextField(default = "", null=True)
    ProjectContributors = models.TextField(default = "", null = True)
    People = models.ManyToManyField('user_functions.Person')
    Goals = models.ManyToManyField('scopes.Goal', through='Goal2Project')
    SpeComs = models.ManyToManyField('scopes.SpeciesCommunity', through='SpeCom2Project')
    ConMeas = models.ManyToManyField('scopes.ConservationMeasure', through='ConMeas2Project')
    Locations = models.ManyToManyField('scopes.Location', through='Location2Project')
    Triggers = models.ManyToManyField('Trigger')
    Outputs = models.ManyToManyField('Output')
    Objectives = models.ManyToManyField('Objective')
    RelatedProjects = models.ManyToManyField('RelatedProject')
    
    
class RelatedProject(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    WorktaskID = models.CharField(default = "", max_length=10)
    RelationshipType = models.CharField(default = "", max_length=100)
    
class Trigger(models.Model):
    ProjectID = models.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
    TriggerName = models.CharField(max_length=38, default = "", null = True)
    TriggerDescription = models.TextField(default = "", null = True)
    TriggerIndicators = models.TextField(default = "", null = True)
    ProposedResponse = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    TriggerStatus = models.ManyToManyField('TriggerStatus')

class TriggerStatus(models.Model):
    TriggerID = models.ForeignKey(Trigger, on_delete=models.CASCADE)
    ReportingDate = models.DateField(null = True)
    StatusTrend = models.TextField(default = "", null = True)
    MgmtInterp = models.TextField(default = "", null = True)
    MgmtResponse = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)

class Output(models.Model):
    ProjectID = models.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
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

class Objective(models.Model):
    ProjectID = models.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
    ObjCode = models.CharField(max_length=25, default = "", null = True)
    ObjName = models.CharField(max_length=100, default = "", null = True)
    ObjDescription = models.TextField(default = "", null = True)
    ObjStartDate = models.DateField(null = True)
    ObjEndDate = models.DateField(null = True)
    ObjFlowDiagram = models.CharField(max_length=255, default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    Milestones = models.ManyToManyField('Milestone')
    Steps = models.ManyToManyField('Step', through='Objective2Step')

class Milestone(models.Model):
    ObjectiveID = models.ForeignKey(Objective, on_delete=models.CASCADE)
    MilestoneID = models.CharField(max_length=25, default = "", null = True)
    MilestoneName = models.CharField(max_length=100, default = "", null = True)
    Description = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    MilestoneProgress = models.ManyToManyField('MilestoneProgress')

class MilestoneProgress(models.Model):
    MilestoneID = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    ReportingDate = models.DateField(null = True)
    Status = models.CharField(max_length=25, default = "", null = True)
    Description = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)

class Step(models.Model):
    ObjectiveID = models.ForeignKey(Objective, on_delete=models.CASCADE)
    StepName = models.CharField(max_length=100, default = "", null = True)
    StepCode = models.CharField(max_length=10, default = "", null = True)
    StepType = models.CharField(max_length=100, default = "", null = True)
    StepSummary = models.TextField(default = "", null = True)
    StepStartDate = models.DateField(null = True)
    StepEndDate = models.DateField(null = True)
    StepDependencies = models.TextField(default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    Methods = models.ManyToManyField('Method', through='Step2Method')

class Method(models.Model):
    StepID = models.ForeignKey(Step, on_delete=models.CASCADE)
    MethodTitle = models.CharField(max_length=255, default = "", null = True)
    MethodCode = models.CharField(max_length=10, default = "", null = True)
    MethodType = models.CharField(max_length=50, default = "", null = True)
    MethodDate = models.DateField(null = True)
    MethodVersion = models.CharField(max_length=10, default = "", null = True)
    MethodDescription = models.TextField(default = "", null = True)
    MethodContact = models.CharField(max_length=38, default = "", null = True)
    Reference = models.TextField(default = "", null=True)
    Protocols = models.ManyToManyField('Protocol', through='Method2Protocol')

class Protocol(models.Model):
    MethodID = models.ForeignKey(Method, on_delete=models.CASCADE)
    ProtocolCode = models.CharField(max_length=10, default = "", null = True)
    ProtocolTitle = models.CharField(max_length=255, default = "", null = True)
    ProtocolVerision = models.CharField(max_length=10, default = "", null = True)
    ProtocolDate = models.DateField(null = True)
    ProtocolAuthor = models.CharField(max_length=255, default = "", null = True)
    ProtocolDescription = models.TextField(default = "", null = True)
    ProtocolLink = models.CharField(max_length=255, default = "", null = True)
    Reference = models.TextField(default = "", null=True)

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