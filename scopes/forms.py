from django import forms
from .models import *
from django.forms import TextInput

class SpeComForm(forms.ModelForm):
    TargetType = forms.CharField(label='Target Type', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Acronym = forms.CharField(label='Acronym', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CommonName = forms.CharField(label='Common Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ScientificName = forms.CharField(label='Scientific Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ITISTSN = forms.CharField(label='ITISTSN', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CommunityName = forms.CharField(label='Community Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Synonyms = forms.CharField(label='Synonyms', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Comments = forms.CharField(label='Comments', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Picture =  forms.ImageField()
    class Meta:
        model = SpeciesCommunity
        fields = '__all__'
        
class LocationForm(forms.ModelForm):
    LocationCode = forms.CharField(label='Location Code', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    LocationName =forms.CharField(label='Location Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Description = forms.CharField(label='Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    SpatialLayer = forms.CharField(label='Spatial Layer', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    SpatialID = forms.CharField(label='Spatial ID', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = Location
        fields = '__all__'
        
class ConMeasureForm(forms.ModelForm):
    CMCode = forms.CharField(label='CM Code', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CMDescription = forms.CharField(label='CM Description', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    SppHab = forms.CharField(label='Spatial Habitat', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CMType = forms.CharField(label='CM Type', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CMSummary = forms.CharField(label='CM Summary', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Status = forms.CharField(label='Status', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))   
    class Meta:
        model = ConservationMeasure
        fields = '__all__'
           
class GoalForm(forms.ModelForm):
    GoalName = forms.CharField(label='Goal Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    GoalType = forms.CharField(label='Goal Type', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    GoalDescription = forms.CharField(label='Goal Description', required = True, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))     
    class Meta:
        model = Goal
        fields = ('GoalName', 'GoalType', 'GoalDescription',)