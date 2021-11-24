from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SpeciesCommunity)
admin.site.register(Location)
admin.site.register(ConservationMeasure)
admin.site.register(Goal)