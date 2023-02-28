from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin

class ClientModelAdmin(VersionAdmin):
    pass

# Register your models here.
@admin.register(SpeciesCommunity)
class SpeciesCommunityAdmin(VersionAdmin):
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

@admin.register(Location)
class LocationAdmin(VersionAdmin):
    search_fields = [
        'LocationCode',
        'LocationName',
        'Description',
        'SpatialLayer',
        'SpatialID',
    ]

@admin.register(ConservationMeasure)
class ConservationMeasureAdmin(VersionAdmin):
    search_fields = [
        'CMCode',
        'CMDescription',
        'SppHab',
        'CMType',
        'CMSummary',
        'Status',
    ]

@admin.register(Goal)
class GoalAdmin(VersionAdmin):
    search_fields = [
        'GoalName',
        'GoalType',
        'GoalDescription',
    ]