from django.db import models
from django import forms
from django.contrib.auth.models import User
#from scopes.models import *
#from projects.models import *

# Create your models here.
class Person(models.Model):
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    Affiliation = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=False)
    Phone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.FirstName + " " + self.LastName
    
    class Meta:
        verbose_name_plural = "People"    
    
class UserProfile(models.Model):
    LEVELS = (
        ('Authorized', 'Authorized'),
        ('Lead', 'Lead'),
        ('Admin', 'Admin'),
    )
    STATUS = (
        ('Unlocked', 'Unlocked'),
        ('Locked', 'Locked'),
    )    
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Level = models.CharField(max_length=12, choices=LEVELS)
    Status = models.CharField(max_length=10, choices=STATUS, default='Unlocked')
    Person = models.OneToOneField(Person, on_delete=models.CASCADE)
    
    '''def __str__(self):
        return self.User'''
    
    class Meta:
        verbose_name_plural = "User Profiles" 
    
class Organization(models.Model):
    Name = models.CharField(max_length=50)
    ContactID = models.OneToOneField(Person, on_delete=models.CASCADE)
    URL = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name_plural = "Organizations" 
        
class Contributor(models.Model):
    #ProjectID = models.OneToOneField('projects.Project', on_delete=models.CASCADE)
    PeopleID = models.ForeignKey(Person, null = True, on_delete=models.CASCADE)
    OrganizationID = models.ForeignKey(Organization, null = True, on_delete=models.CASCADE)
    
'''
class ChangeLog(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Date = models.DateField()
    Content = models.TextField()
    Location = models.TextField()
''' 
    