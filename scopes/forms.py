from django import forms
from .models import *
from django.forms import TextInput, Select

class SpeComForm(forms.ModelForm):
    TYPES = (
        ('Species', 'Species'),
        ('Ecological Comunity', 'Ecological Comunity'),
    )    
    TargetType = forms.ChoiceField(label='Target Type', choices=TYPES, required = False, widget=forms.Select(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Acronym = forms.CharField(label='Acronym', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CommonName = forms.CharField(label='Common Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ScientificName = forms.CharField(label='Scientific Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    ITISTSN = forms.CharField(label='ITISTSN', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CommunityName = forms.CharField(label='Community Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Synonyms = forms.CharField(label='Synonyms', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Comments = forms.CharField(label='Comments', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Picture =  forms.ImageField()
    class Meta:
        model = SpeciesCommunity
        fields = '__all__'
        
class LocationForm(forms.ModelForm):
    LocationCode = forms.CharField(label='Location Code', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    LocationName =forms.CharField(label='Location Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Description = forms.CharField(label='Description', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    SpatialLayer = forms.CharField(label='Spatial Layer', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    SpatialID = forms.CharField(label='Spatial ID', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))    
    class Meta:
        model = Location
        fields = '__all__'
        
class ConMeasureForm(forms.ModelForm):
    CMCode = forms.CharField(label='CM Code', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CMDescription = forms.CharField(label='CM Description', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    SppHab = forms.CharField(label='Spatial Habitat', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CMType = forms.CharField(label='CM Type', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    CMSummary = forms.CharField(label='CM Summary', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    Status = forms.CharField(label='Status', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))   
    class Meta:
        model = ConservationMeasure
        fields = '__all__'
           
class GoalForm(forms.ModelForm):
    GoalName = forms.CharField(label='Goal Name', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    GoalType = forms.CharField(label='Goal Type', required = False, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))
    GoalDescription = forms.CharField(label='Goal Description', required = False, widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control', 'readonly': 'readonly'}))     
    class Meta:
        model = Goal
        fields = ('GoalName', 'GoalType', 'GoalDescription',)