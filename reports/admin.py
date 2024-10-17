from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CustomTemplate)
class CustomTemplateAdmin(admin.ModelAdmin):
    pass