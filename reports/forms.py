from django import forms

class reportSelectorForm (forms.Form):
    projectToggle = forms.BooleanField(label='Project', error_messages={'required': 'Select at least one field to be added to the project report'},   widget=forms.CheckboxInput(attrs={'checked': True}))
    triggerToggle = forms.BooleanField(label='Trigger', required = False,)
    triggerStatusToggle = forms.BooleanField(label='Trigger Status', required = False,)
    objectiveToggle = forms.BooleanField(label='Objective', required = False,)
    milestoneToggle = forms.BooleanField(label='Milestone', required = False,)
    stepToggle = forms.BooleanField(label='Step', required = False,)
    methodToggle = forms.BooleanField(label='Method', required = False,)
    protocolToggle = forms.BooleanField(label='Protocol', required = False,)
    outputToggle = forms.BooleanField(label='Output', required = False,)

    
