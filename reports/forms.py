from django import forms
from django.db import models
from .models import *
import projects.models as pr

class TriggerMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.TriggerName
    
class TriggerStatusMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.ReportingDate
    
class ObjectiveMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.ObjCode
    
class MilestoneMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.MilestoneName
    
class StepMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.StepName
    
class MethodMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.MethodTitle   
    
class ProtocolMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.ProtocolTitle
    
class OutputMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.OutputTitle    
    
class templateUploadForm(forms.ModelForm):
    template = forms.ModelChoiceField(label='Select', queryset=CustomTemplate.objects.all(), required = False,)
    file = forms.FileField(label='Upload', required = False,)
    class Meta:
        model = CustomTemplate
        fields = ('file',)
    
class reportSelectorForm (forms.Form):
    def __init__(self, projectID, *args, **kwargs):
        super(reportSelectorForm, self).__init__(*args, **kwargs)
        self.fields['projectToggle'] = forms.BooleanField(label='Project', error_messages={'required': 'Select at least one field to be added to the project report'},   widget=forms.CheckboxInput(attrs={'checked': True}))
        self.fields['triggerToggle'] = forms.BooleanField(label='Trigger', required = False, widget=forms.CheckboxInput( attrs = {'id':'triggerToggle', 'onclick':'secondaryToggle("triggers")'}))
        self.fields['triggers'] = TriggerMultipleChoiceField(queryset=pr.Trigger.objects.filter(ProjectID = projectID), widget=forms.CheckboxSelectMultiple(attrs={'class':'triggers', 'onclick':'masterToggle("triggerToggle")'}), required = False, )    
        self.fields['triggerStatusToggle'] = forms.BooleanField(label='Trigger Status', required = False, widget=forms.CheckboxInput( attrs = {'id':'triggerStatusToggle', 'onclick':'secondaryToggle("triggerStatuses")'}))
        self.fields['triggerStatuses'] = TriggerStatusMultipleChoiceField(queryset=pr.TriggerStatus.objects.filter(trigger__project__id = projectID), widget=forms.CheckboxSelectMultiple(attrs={'class':'triggerStatuses', 'onclick':'masterToggle("triggerStatusToggle")'}), required = False, )
        self.fields['objectiveToggle'] = forms.BooleanField(label='Objective', required = False, widget=forms.CheckboxInput( attrs = {'id':'objectiveToggle', 'onclick':'secondaryToggle("objectives")'}))
        self.fields['objectives'] = ObjectiveMultipleChoiceField(queryset=pr.Objective.objects.filter(ProjectID = projectID), widget=forms.CheckboxSelectMultiple(attrs={'class':'objectives', 'onclick':'masterToggle("objectiveToggle")'}), required = False, )
        self.fields['milestoneToggle'] = forms.BooleanField(label='Milestone', required = False, widget=forms.CheckboxInput( attrs = {'id':'milestoneToggle', 'onclick':'secondaryToggle("milestones")'}))
        self.fields['milestones'] = MilestoneMultipleChoiceField(queryset=pr.Milestone.objects.filter(objective__project__id = projectID), widget=forms.CheckboxSelectMultiple(attrs={'class':'milestones', 'onclick':'masterToggle("milestoneToggle")'}), required = False, )
        self.fields['stepToggle'] = forms.BooleanField(label='Step', required = False, widget=forms.CheckboxInput( attrs = {'id':'stepToggle', 'onclick':'secondaryToggle("steps")'}))
        self.fields['steps'] = StepMultipleChoiceField(queryset=pr.Step.objects.filter(objective__project__id = projectID), widget=forms.CheckboxSelectMultiple(attrs={'class':'steps', 'onclick':'masterToggle("stepToggle")'}), required = False, )
        self.fields['methodToggle'] = forms.BooleanField(label='Method', required = False, widget=forms.CheckboxInput( attrs = {'id':'methodToggle', 'onclick':'secondaryToggle("methods")'}))
        self.fields['methods'] = MethodMultipleChoiceField(queryset=pr.Method.objects.filter(step__objective__project__id = projectID), widget=forms.CheckboxSelectMultiple(attrs={'class':'methods', 'onclick':'masterToggle("methodToggle")'}), required = False, )
        self.fields['protocolToggle'] = forms.BooleanField(label='Protocol', required = False, widget=forms.CheckboxInput( attrs = {'id':'protocolToggle', 'onclick':'secondaryToggle("protocols")'}))
        self.fields['protocols'] = ProtocolMultipleChoiceField(queryset=pr.Protocol.objects.filter(method__step__objective__project__id = projectID), widget=forms.CheckboxSelectMultiple(attrs={'class':'protocols', 'onclick':'masterToggle("protocolToggle")'}), required = False, )
        self.fields['outputToggle'] = forms.BooleanField(label='Output', required = False, widget=forms.CheckboxInput( attrs = {'id':'outputToggle', 'onclick':'secondaryToggle("outputs")'}))
        self.fields['outputs'] = OutputMultipleChoiceField(queryset=pr.Output.objects.filter(ProjectID = projectID), widget=forms.CheckboxSelectMultiple(attrs={'class':'outputs', 'onclick':'masterToggle("outputToggle")'}), required = False,)  
    '''class Meta:
        model = pr.Project
        fields = ('template','projectToggle','triggerToggle','triggers','triggerStatusToggle','triggerStatuses','objectiveToggle','objectives','milestoneToggle','milestones','','stepToggle','steps','methodToggle','methods','protocolToggle','protocols','outputToggle','outputs',)
'''
    
