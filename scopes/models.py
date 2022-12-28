from django.db import models
from django import forms
#from projects.models import *
#from user_functions.models import *

# Create your models here.

class SpeciesCommunity(models.Model):
    TYPES = (
        ('Species', 'Species'),
        ('Ecological Comunity', 'Ecological Comunity'),
    )
    
    TargetType = models.CharField(max_length=25, choices = TYPES, null = True)
    Acronym = models.CharField(max_length=10, default = "", null = True)
    CommonName = models.CharField(max_length=255, default = "", null = True)
    ScientificName = models.CharField(max_length=255, default = "", null = True)
    ITISTSN = models.CharField(max_length=8, default = "", null = True)
    CommunityName = models.CharField(max_length=255, default = "", null = True)
    Synonyms = models.TextField(default = "", null = True)
    Comments = models.TextField(default = "", null = True)
    Picture = models.ImageField(upload_to='SpeCom', default = '../media/default.png', null=True, blank=False)
    
    def __str__(self):
        return self.CommonName
    
    class Meta:
        verbose_name_plural = "Species/Communities"     

class Location(models.Model):
    LocationCode = models.CharField(max_length=10, default = "", null = True)
    LocationName = models.CharField(max_length=255, default = "", null = True)
    Description = models.TextField(default = "", null = True)
    SpatialLayer = models.TextField(default = "", null = True)
    SpatialID = models.CharField(max_length=25, default = "", null = True)
    
    def __str__(self):
        return self.LocationCode
    
    class Meta:
        verbose_name_plural = "Locations"     
    
class ConservationMeasure(models.Model):
    CMCode = models.CharField(max_length=10, default = "", null = True)
    CMDescription = models.CharField(max_length=100, default = "", null = True)
    SppHab = models.CharField(max_length=100, default = "", null = True)
    CMType = models.CharField(max_length=50, default = "",null = True)
    CMSummary = models.TextField(default = "", null = True)
    Status = models.CharField(max_length=10, default = "", null = True)
    
    def __str__(self):
        return self.CMCode
    
    class Meta:
        verbose_name_plural = "Conservation Measures"     

class Goal(models.Model):
    GoalName = models.CharField(max_length=255, default = "", null = True)
    GoalType = models.CharField(max_length=50, default = "", null = True)
    GoalDescription = models.TextField(default = "", null = True)
    
    def __str__(self):
        return self.GoalName
    
    class Meta:
        verbose_name_plural = "Goals"     
    
