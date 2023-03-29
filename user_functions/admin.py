from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin
from advanced_filters.admin import AdminAdvancedFiltersMixin

class ClientModelAdmin(VersionAdmin):
    pass

# Register your models here.
@admin.register(Person)
class PersonAdmin(AdminAdvancedFiltersMixin, VersionAdmin):
    search_fields = [
        'LastName',
        'FirstName',
        'Affiliation',
        'Address',
        'Email',
        'Phone',
    ]
    
    advanced_filter_fields = (
        ('LastName', 'Last Name'),
        ('FirstName', 'First Name'),
        ('Affiliation', 'Affiliation'),
        ('Address', 'Address'),
        ('Email', 'Email'),
        ('Phone', 'Phone'),
    )    

@admin.register(UserProfile)
class UserProfileAdmin(AdminAdvancedFiltersMixin, VersionAdmin):
    search_fields = [
        'Level',
        'Status',
        'Person__LastName',
        'Person__FirstName',      
    ]
    
    advanced_filter_fields = (
        ('Level', 'Level'),
        ('Status', 'Status'),
        ('Person__LastName', 'Last Name'),
        ('Person__FirstName', 'First Name'),       
    )    

@admin.register(Organization)
class OrganizationAdmin(AdminAdvancedFiltersMixin, VersionAdmin):
    search_fields = [
        'Name',
        'ContactID__LastName',
        'ContactID__FirstName',
        'URL',
        'Address',
        'Email',
        'Phone',        
    ]
    
    advanced_filter_fields = (
        ('Name', 'Name'),
        ('ContactID__LastName', 'Last Name'),
        ('ContactID__FirstName', 'First Name'),
        ('URL', 'URL'),
        ('Address', 'Address'),
        ('Email', 'Email'),
        ('Phone', 'Phone Number'),        
    )    