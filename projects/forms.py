from django import forms
from .models import *
from django.db import models
from scopes.models import *
from django.forms import TextInput, DateInput, Select
from django.core.exceptions import ValidationError
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
import datetime

def validate_date(value):
    print("validated")
    if isinstance(value, datetime.date):
        print("not a date")
        raise ValidationError(
            ('%(value)s is not a valid date'),
            params={'value': value},
        )        

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
    WorktaskID = forms.CharField(label='Worktask ID', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProjectName = forms.CharField(label='Project Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProjectLead = forms.CharField(label='Project Lead', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProjectStatus = forms.ChoiceField(label='Project Status', choices = STATUS_CHOICES, required = False, widget=forms.Select(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProjectType = forms.ChoiceField(label='Project Type', choices = TYPE_CHOICES, required = False, widget=forms.Select(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProjectStart = forms.DateField(label='Project Start', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))#, validators=[validate_date])
    ProjectEnd = forms.DateField(label='Project End', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))#, validators=[validate_date])
    ProjectSummary = forms.CharField(label='Project Summary', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProjectBackground = forms.CharField(label='Project Background', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OtherConsMeas = forms.CharField(label='Other Conservation Measure', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OtherSpecies = forms.CharField(label='Other Species', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Contributor = forms.CharField(label='Contributors', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    
    class Meta:
        model = Project
        exclude = ('ProjectContributors','People','Goals','SpeComs','ConMeas','Locations','Triggers','Outputs','Objectives','RelatedProjects',)

class TriggerHelperForm(forms.Form):
    class Meta:
        model = Trigger
        fields = ()
        
class OutputHelperForm(forms.Form):
    class Meta:
        model = Output
        fields = ()
        
class ObjectiveHelperForm(forms.Form):
    class Meta:
        model = Objective
        fields = ()

class SpeComMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.CommonName

class ConMeasMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.CMCode

class LocationMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.LocationCode
    
class GoalMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.GoalName    

class SpeComAdderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):   
        super(SpeComAdderForm, self).__init__(*args, **kwargs)
        self.fields['speComs'] = SpeComMultipleChoiceField(queryset=SpeciesCommunity.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Project
        fields = ('SpeComs',)
        
class ConMeasAdderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):   
        super(ConMeasAdderForm, self).__init__(*args, **kwargs)
        self.fields['conMeas'] = ConMeasMultipleChoiceField(queryset=ConservationMeasure.objects.all(), widget=forms.CheckboxSelectMultiple(), required = False,)            
    #ConMeas = ConMeasMultipleChoiceField(queryset=ConservationMeasure.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Project
        fields = ('ConMeas',)
    
class LocationAdderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):   
        super(LocationAdderForm, self).__init__(*args, **kwargs)
        self.fields['locations'] = LocationMultipleChoiceField(queryset=Location.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Project
        fields = ('Locations',)
    
class GoalAdderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):   
        super(GoalAdderForm, self).__init__(*args, **kwargs)
        self.fields['goals'] = GoalMultipleChoiceField(queryset=Goal.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Project
        fields = ('Goals',)
        
class RelatedProjectHelperForm(forms.Form):
    class Meta:
        model = RelatedProject
        fields = ()

class RelatedProjectForm(forms.ModelForm):
    WorktaskID = forms.CharField(label='Worktask ID', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    RelationshipType = forms.CharField(label='Relationship Type', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))    
    class Meta:
        model = RelatedProject
        exclude = ('Project',)
        
class TriggerForm(forms.ModelForm):
    TriggerName = forms.CharField(label='Trigger Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    TriggerDescription = forms.CharField(label='Trigger Description', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    TriggerIndicators = forms.CharField(label='Trigger Indicators', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProposedResponse = forms.CharField(label='Proposed Response', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))    
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = Trigger
        exclude = ('ProjectID','TriggerStatus',)
        
class TriggerStatusForm(forms.ModelForm):
    ReportingDate = forms.DateField(label='Reporting Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    StatusTrend = forms.CharField(label='Status Trend', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MgmtInterp = forms.CharField(label='Management Interpretation', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MgmtResponse = forms.CharField(label='Management Response', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))   
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = TriggerStatus
        exclude = ('TriggerID',)

class TriggerStatusHelperForm(forms.Form):
    class Meta:
        model = TriggerStatus
        fields = ()
        
class OutputForm(forms.ModelForm):
    OutputType = forms.CharField(label='Output Type', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputAuthors = forms.CharField(label='Output Authors', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputDate = forms.DateField(label='Output Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputTitle = forms.CharField(label='Output Title', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputVersion = forms.CharField(label='Output Version', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputDescription = forms.CharField(label='Output Description', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputDOI = forms.CharField(label='Output DOI', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputCitation = forms.CharField(label='Output Citation', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputURI = forms.CharField(label='Output URI', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    OutputConstraints = forms.CharField(label='Output Constraints', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))    
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = Output
        exclude = ('ProjectID',)
        
class ObjectiveForm(forms.ModelForm):
    ObjCode = forms.CharField(label='Objective Code', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ObjName = forms.CharField(label='Objective Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ObjDescription = forms.CharField(label='Objective Description', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ObjStartDate = forms.DateField(label='Objective Start Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ObjEndDate = forms.DateField(label='Objective End Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ObjFlowDiagram = forms.CharField(label='Objective Flow Diagram', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = Objective
        exclude = ('ProjectID','Milestones','Steps',)
        
class MilestoneHelperForm(forms.Form):
    class Meta:
        model = Milestone
        fields = ()
        
class MilestoneForm(forms.ModelForm):
    MilestoneID = forms.CharField(label='ID', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MilestoneName = forms.CharField(label='Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))    
    Description = forms.CharField(label='Description', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = Milestone
        exclude = ('ObjectiveID','MilestoneProgress',)
        
class MilestoneProgressHelperForm(forms.Form):
    class Meta:
        model = MilestoneProgress
        fields = ()
        
class MilestoneProgressForm(forms.ModelForm):
    ReportingDate = forms.DateField(label='Reporting Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Status = forms.CharField(label='Status', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Description =forms.CharField(label='Description', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))    
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = MilestoneProgress
        exclude = ('MilestoneID',)

class StepHelperForm(forms.Form):
    class Meta:
        model = Step
        fields = ()

class StepForm(forms.ModelForm):
    StepName = forms.CharField(label='Step Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    StepCode = forms.CharField(label='Step Code', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    StepType = forms.CharField(label='Step Type', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    StepSummary = forms.CharField(label='Step Summary', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    StepStartDate = forms.DateField(label='Step Start Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    StepEndDate = forms.DateField(label='Step End Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    StepDependencies = forms.CharField(label='Step Dependencies', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))    
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = Step
        exclude = ('Methods','ObjectiveID',)
        
class MethodHelperForm(forms.Form):
    class Meta:
        model = Method
        fields = ()
        
class MethodForm(forms.ModelForm):
    MethodTitle = forms.CharField(label='Method Title', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MethodCode = forms.CharField(label='Method Code', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MethodType = forms.CharField(label='Method Type', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MethodDate = forms.DateField(label='Method Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MethodVersion = forms.CharField(label='Method Version', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MethodDescription = forms.CharField(label='Method Description', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    MethodContact = forms.CharField(label='Method Contact', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))    
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = Method
        exclude = ('Protocols', 'StepID',)
        
class ProtocolHelperForm(forms.Form):
    class Meta:
        model = Protocol
        fields = ()
                
class ProtocolForm(forms.ModelForm):
    ProtocolCode = forms.CharField(label='Protocol Code', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProtocolTitle = forms.CharField(label='Protocol Title', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProtocolVerision = forms.CharField(label='Protocol Verision', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProtocolDate = forms.DateField(label='Protocol Date', required = False, widget=forms.DateInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProtocolAuthor = forms.CharField(label='Protocol Author', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProtocolDescription = forms.CharField(label='Protocol Description', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    ProtocolLink = forms.CharField(label='Protocol Link', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))    
    Reference = forms.CharField(label='Reference', required = False, widget=SummernoteWidget(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    class Meta:
        model = Protocol
        exclude = ('MethodID',)
        