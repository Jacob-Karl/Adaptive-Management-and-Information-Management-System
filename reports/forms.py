from django import forms

class reportSelectorForm (forms.Form):
    projectToggle = forms.BooleanField(label='Project', required = False,)
    triggerToggle = forms.BooleanField(label='Trigger', required = False,)
    triggerStatusToggle = forms.BooleanField(label='Trigger Status', required = False,)
    objectiveToggle = forms.BooleanField(label='Objective', required = False,)
    milestoneToggle = forms.BooleanField(label='Milestone', required = False,)
    stepToggle = forms.BooleanField(label='Step', required = False,)
    methodToggle = forms.BooleanField(label='Method', required = False,)
    protocolToggle = forms.BooleanField(label='Protocol', required = False,)    
    outputPath = forms.FilePathField(path = '..\..\..', allow_files = False, allow_folders = True, recursive = True, label='Output',)