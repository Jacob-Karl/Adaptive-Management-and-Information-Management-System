from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin
from advanced_filters.admin import AdminAdvancedFiltersMixin

class ClientModelAdmin(VersionAdmin):
    pass

# Register your models here.
@admin.register(SpeciesCommunity)
class SpeciesCommunityAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
    search_fields = [
        'TargetType',
        'Acronym',
        'CommonName',
        'ScientificName',
        'ITISTSN',
        'CommunityName',
        'Synonyms',
        'Comments',
    ]
    
    advanced_filter_fields = (
        ('TargetType', 'Target Type'),
        ('Acronym', 'Acronym'),
        ('CommonName', 'Common Name'),
        ('ScientificName', 'Scientific Name'),
        ('ITISTSN','ITISTSN'),
        ('CommunityName', 'CommunityName'),
        ('Synonyms', 'Synonyms'),
        ('Comments', 'Comments'),
        
    )

@admin.register(Location)
class LocationAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
    search_fields = [
        'LocationCode',
        'LocationName',
        'Description',
        'SpatialLayer',
        'SpatialID',
    ]
    
    advanced_filter_fields = (
        ('LocationCode', 'Location Code'),
        ('LocationName', 'Location Name'),
        ('Description', 'Description'),
        ('SpatialLayer', 'Spatial Layer'),
        ('SpatialID', 'Spatial ID'),    
    )    

@admin.register(ConservationMeasure)
class ConservationMeasureAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
    search_fields = [
        'CMCode',
        'CMDescription',
        'SppHab',
        'CMType',
        'CMSummary',
        'Status',
    ]
    
    advanced_filter_fields = (
        ('CMCode', 'Conservation Measure Code'),
        ('CMDescription', 'Conservation Measure Description'),
        ('SppHab', 'Spatial Habitat'),
        ('CMType', 'Conservation Measure Type'),
        ('CMSummary', 'Conservation Measure Summary'),
        ('Status', 'Status'),    
    )    

@admin.register(Goal)
class GoalAdmin(AdminAdvancedFiltersMixin, CompareVersionAdmin):
    search_fields = [
        'GoalName',
        'GoalType',
        'GoalDescription',
    ]
    
    advanced_filter_fields = (
        ('GoalName', 'Goal Name'),
        ('GoalType', 'Goal Type'),
        ('GoalDescription', 'Goal Description'),        
    )    