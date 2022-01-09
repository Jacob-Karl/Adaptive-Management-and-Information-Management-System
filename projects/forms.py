from django import forms
from .models import *
from django.db import models
from scopes.models import *
from django.forms import TextInput, DateInput, Select

class ProjectForm(forms.ModelForm):
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
    WorktaskID = forms.CharField(label='Worktask ID', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProjectName = forms.CharField(label='Project Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProjectLead = forms.CharField(label='Project Lead', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProjectStatus = forms.ChoiceField(label='Project Status', choices = STATUS_CHOICES, required = False, widget=forms.Select(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProjectType = forms.ChoiceField(label='Project Type', choices = TYPE_CHOICES, required = False, widget=forms.Select(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProjectStart = forms.DateField(label='Project Start', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProjectEnd = forms.DateField(label='Project End', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProjectSummary = forms.CharField(label='Project Summary', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProjectBackground = forms.CharField(label='Project Background', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OtherConsMeas = forms.CharField(label='Other Conservation Measure', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OtherSpecies = forms.CharField(label='Other Species', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    class Meta:
        model = Project
        exclude = ('ProjectContributors','People','Goals','SpeComs','ConMeas','Locations','Triggers','Outputs','Objectives','RelatedProjects',)

class TriggerHelperForm(forms.Form):
    class Meta:
        model = Trigger
        fields = ()

class GoalAdderForm(forms.ModelForm):
    Goals = forms.ModelMultipleChoiceField(queryset=Goal.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Project
        fields = ('Goals',)

class RelatedProjectForm(forms.ModelForm):
    WorktaskID = forms.CharField(label='Worktask ID', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    RelationshipType = forms.CharField(label='Relationship Type', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = RelatedProject
        fields = '__all__'
        
class TriggerForm(forms.ModelForm):
    TriggerName = forms.CharField(label='Trigger Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    TriggerDescription = forms.CharField(label='Trigger Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    TriggerIndicators = forms.CharField(label='Trigger Indicators', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProposedResponse = forms.CharField(label='Proposed Response', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = Trigger
        exclude = ('ProjectID','TriggerStatus',)
        
class TriggerStatusForm(forms.ModelForm):
    ReportingDate = forms.DateField(label='Reporting Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    StatusTrend = forms.CharField(label='Status Trend', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    MgmtInterp = forms.CharField(label='Management Interpretation', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    MgmtResponse = forms.CharField(label='Management Response', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))   
    class Meta:
        model = TriggerStatus
        fields = '__all__'
        
class OutputForm(forms.ModelForm):
    OutputType = forms.CharField(label='Output Type', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputAuthors = forms.CharField(label='Output Authors', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputDate = forms.DateField(label='Output Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputTitle = forms.CharField(label='Output Title', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputVersion = forms.CharField(label='Output Version', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputDescription = forms.CharField(label='Output Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputDOI = forms.CharField(label='Output DOI', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputCitation = forms.CharField(label='Output Citation', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputURI = forms.CharField(label='Output URI', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    OutputConstraints = forms.CharField(label='Output Constraints', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = Output
        fields = '__all__'
        
class ObjectiveForm(forms.ModelForm):
    ObjCode = forms.CharField(label='Objective Code', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ObjName = forms.CharField(label='Objective Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ObjDescription = forms.CharField(label='Objective Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ObjStartDate = forms.DateField(label='Objective Start Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ObjEndDate = forms.DateField(label='Objective End Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ObjFlowDiagram = forms.CharField(label='Objective Flow Diagram', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    class Meta:
        model = Objective
        exclude = ('Milestones','Steps',)
        
class MilestoneForm(forms.ModelForm):
    Description = forms.CharField(label='Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    class Meta:
        model = Milestone
        exclude = ('MilestoneProgress',)
        
class MilestoneProgressForm(forms.ModelForm):
    ReportingDate = forms.DateField(label='Reporting Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Status = forms.CharField(label='Status', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Description =forms.CharField(label='Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = MilestoneProgress
        fields = '__all__'

class StepForm(forms.ModelForm):
    StepName = forms.CharField(label='Step Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    StepCode = forms.CharField(label='Step Code', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    StepType = forms.CharField(label='Step Type', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    StepSummary = forms.CharField(label='Step Summary', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    StepStartDate = forms.DateField(label='Step Start Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    StepEndDate = forms.DateField(label='Step End Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    StepDependencies = forms.CharField(label='Step Dependencies', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = Step
        exclude = ('Methods',)
        
class MethodForm(forms.ModelForm):
    MethodTitle = forms.CharField(label='Method Title', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    MethodCode = forms.CharField(label='Method Code', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    MethodType = forms.CharField(label='Method Type', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    MethodDate = forms.DateField(label='Method Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    MethodVersion = forms.CharField(label='Method Version', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    MethodDescription = forms.CharField(label='Method Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    MethodContact = forms.CharField(label='Method Contact', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = Method
        exclude = ('Protocols',)
        
class ProtocolForm(forms.ModelForm):
    ProtocolTitle = forms.CharField(label='Protocol Title', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProtocolVerision = forms.CharField(label='Protocol Verision', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProtocolDate = forms.DateField(label='Protocol Date', required = True, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProtocolAuthor = forms.CharField(label='Protocol Author', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProtocolDescription = forms.CharField(label='Protocol Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ProtocolLink = forms.CharField(label='Protocol Link', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = Protocol
        fields = '__all__'
        