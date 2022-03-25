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
    Acronym = models.CharField(max_length=10, null = True)
    CommonName = models.CharField(max_length=255, null = True)
    ScientificName = models.CharField(max_length=255, null = True)
    ITISTSN = models.CharField(max_length=8, null = True)
    CommunityName = models.CharField(max_length=255, null = True)
    Synonyms = models.TextField(null = True)
    Comments = models.TextField(null = True)
    Picture = models.ImageField(upload_to='SpeCom', default = '../media/default.png', null=True, blank=False)

class Location(models.Model):
    LocationCode = models.CharField(max_length=10, null = True)
    LocationName = models.CharField(max_length=255, null = True)
    Description = models.TextField(null = True)
    SpatialLayer = models.TextField(null = True)
    SpatialID = models.CharField(max_length=25, null = True)
    
class ConservationMeasure(models.Model):
    CMCode = models.CharField(max_length=10, null = True)
    CMDescription = models.CharField(max_length=100, null = True)
    SppHab = models.CharField(max_length=100, null = True)
    CMType = models.CharField(max_length=50, null = True)
    CMSummary = models.TextField(null = True)
    Status = models.CharField(max_length=10, null = True)

class Goal(models.Model):
    GoalName = models.CharField(max_length=255, null = True)
    GoalType = models.CharField(max_length=50, null = True)
    GoalDescription = models.TextField(null = True)
    
