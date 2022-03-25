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
    
    TargetType = models.CharField(max_length=25, choices = TYPES)
    Acronym = models.CharField(max_length=10)
    CommonName = models.CharField(max_length=255)
    ScientificName = models.CharField(max_length=255)
    ITISTSN = models.CharField(max_length=8)
    CommunityName = models.CharField(max_length=255)
    Synonyms = models.TextField()
    Comments = models.TextField()
    Picture = models.ImageField(upload_to='SpeCom', default = '../media/default.png', null=False, blank=False)

class Location(models.Model):
    LocationCode = models.CharField(max_length=10)
    LocationName = models.CharField(max_length=255)
    Description = models.TextField()
    SpatialLayer = models.TextField()
    SpatialID = models.CharField(max_length=25)
    
class ConservationMeasure(models.Model):
    CMCode = models.CharField(max_length=10)
    CMDescription = models.CharField(max_length=100)
    SppHab = models.CharField(max_length=100)
    CMType = models.CharField(max_length=50)
    CMSummary = models.TextField()
    Status = models.CharField(max_length=10)

class Goal(models.Model):
    GoalName = models.CharField(max_length=255)
    GoalType = models.CharField(max_length=50)
    GoalDescription = models.TextField()
    
