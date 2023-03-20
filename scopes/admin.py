from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin
from advanced_filters.admin import AdminAdvancedFiltersMixin

class ClientModelAdmin(VersionAdmin):
    pass

# Register your models here.
@admin.register(SpeciesCommunity)
class SpeciesCommunityAdmin(AdminAdvancedFiltersMixin, VersionAdmin):
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
        'TargetType',
        'Acronym',
        'CommonName',
        'ScientificName',
        'ITISTSN',
        'CommunityName',
        'Synonyms',
        'Comments',
        
    )

@admin.register(Location)
class LocationAdmin(AdminAdvancedFiltersMixin, VersionAdmin):
    search_fields = [
        'LocationCode',
        'LocationName',
        'Description',
        'SpatialLayer',
        'SpatialID',
    ]
    
    advanced_filter_fields = (
        'LocationCode',
        'LocationName',
        'Description',
        'SpatialLayer',
        'SpatialID',        
    )    

@admin.register(ConservationMeasure)
class ConservationMeasureAdmin(AdminAdvancedFiltersMixin, VersionAdmin):
    search_fields = [
        'CMCode',
        'CMDescription',
        'SppHab',
        'CMType',
        'CMSummary',
        'Status',
    ]
    
    advanced_filter_fields = (
        'CMCode',
        'CMDescription',
        'SppHab',
        'CMType',
        'CMSummary',
        'Status',        
    )    

@admin.register(Goal)
class GoalAdmin(AdminAdvancedFiltersMixin, VersionAdmin):
    search_fields = [
        'GoalName',
        'GoalType',
        'GoalDescription',
    ]
    
    advanced_filter_fields = (
        'GoalName',
        'GoalType',
        'GoalDescription',        
    )    