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
    
    WorktaskID = models.CharField(max_length=10, null = True)
    ProjectName = models.CharField(max_length=255, null = True)
    ProjectLead = models.CharField(max_length=38, null = True)
    ProjectStatus = models.CharField(max_length=10, choices = STATUS_CHOICES, null = True)
    ProjectType = models.CharField(max_length=50, choices = TYPE_CHOICES, null = True)
    ProjectStart = models.DateField(null = True)
    ProjectEnd = models.DateField(null = True)
    ProjectSummary = models.TextField(null = True)
    ProjectBackground = models.TextField(null = True)
    OtherConsMeas = models.CharField(max_length=255, null = True)
    OtherSpecies = models.CharField(max_length=255, null = True)
    Reference = models.TextField(null=True)
    ProjectContributors = models.ManyToManyField('user_functions.Contributor')
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
    WorktaskID = models.CharField(max_length=10)
    RelationshipType = models.CharField(max_length=100)
    
class Trigger(models.Model):
    ProjectID = models.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
    TriggerName = models.CharField(max_length=38, null = True)
    TriggerDescription = models.TextField(null = True)
    TriggerIndicators = models.TextField(null = True)
    ProposedResponse = models.TextField(null = True)
    Reference = models.TextField(null=True)
    TriggerStatus = models.ManyToManyField('TriggerStatus')

class TriggerStatus(models.Model):
    TriggerID = models.ForeignKey(Trigger, on_delete=models.CASCADE)
    ReportingDate = models.DateField(null = True)
    StatusTrend = models.TextField(null = True)
    MgmtInterp = models.TextField(null = True)
    MgmtResponse = models.TextField(null = True)
    Reference = models.TextField(null=True)

class Output(models.Model):
    ProjectID = models.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
    OutputType = models.CharField(max_length=100, null = True)
    OutputAuthors = models.CharField(max_length=255, null = True)
    OutputDate = models.DateField(null = True)
    OutputTitle = models.TextField(null = True)
    OutputVersion = models.CharField(max_length=10, null = True)
    OutputDescription = models.TextField(null = True)
    OutputDOI = models.CharField(max_length=100, null = True)
    OutputCitation = models.TextField(null = True)
    OutputURI = models.CharField(max_length=255, null = True)
    OutputConstraints = models.TextField(null = True)
    Reference = models.TextField(null=True)

class Objective(models.Model):
    ProjectID = models.ForeignKey(Project, unique = False, on_delete=models.CASCADE)
    ObjCode = models.CharField(max_length=25, null = True)
    ObjName = models.CharField(max_length=100, null = True)
    ObjDescription = models.TextField(null = True)
    ObjStartDate = models.DateField(null = True)
    ObjEndDate = models.DateField(null = True)
    ObjFlowDiagram = models.CharField(max_length=255, null = True)
    Reference = models.TextField(null=True)
    Milestones = models.ManyToManyField('Milestone')
    Steps = models.ManyToManyField('Step', through='Objective2Step')

class Milestone(models.Model):
    ObjectiveID = models.ForeignKey(Objective, on_delete=models.CASCADE)
    Description = models.TextField(null = True)
    Reference = models.TextField(null=True)
    MilestoneProgress = models.ManyToManyField('MilestoneProgress')

class MilestoneProgress(models.Model):
    MilestoneID = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    ReportingDate = models.DateField(null = True)
    Status = models.CharField(max_length=25, null = True)
    Description = models.TextField(null = True)
    Reference = models.TextField(null=True)

class Step(models.Model):
    ObjectiveID = models.ForeignKey(Objective, on_delete=models.CASCADE)
    StepName = models.CharField(max_length=100, null = True)
    StepCode = models.CharField(max_length=10, null = True)
    StepType = models.CharField(max_length=100, null = True)
    StepSummary = models.TextField(null = True)
    StepStartDate = models.DateField(null = True)
    StepEndDate = models.DateField(null = True)
    StepDependencies = models.TextField(null = True)
    Reference = models.TextField(null=True)
    Methods = models.ManyToManyField('Method', through='Step2Method')

class Method(models.Model):
    StepID = models.ForeignKey(Step, on_delete=models.CASCADE)
    MethodTitle = models.CharField(max_length=255, null = True)
    MethodCode = models.CharField(max_length=10, null = True)
    MethodType = models.CharField(max_length=50, null = True)
    MethodDate = models.DateField(null = True)
    MethodVersion = models.CharField(max_length=10, null = True)
    MethodDescription = models.TextField(null = True)
    MethodContact = models.CharField(max_length=38, null = True)
    Reference = models.TextField(null=True)
    Protocols = models.ManyToManyField('Protocol', through='Method2Protocol')

class Protocol(models.Model):
    MethodID = models.ForeignKey(Method, on_delete=models.CASCADE)
    ProtocolTitle = models.CharField(max_length=255, null = True)
    ProtocolVerision = models.CharField(max_length=10, null = True)
    ProtocolDate = models.DateField(null = True)
    ProtocolAuthor = models.CharField(max_length=255, null = True)
    ProtocolDescription = models.TextField(null = True)
    ProtocolLink = models.CharField(max_length=255, null = True)
    Reference = models.TextField(null=True)

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