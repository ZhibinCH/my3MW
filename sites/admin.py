from django.contrib import admin
from sites.models import *

@admin.register(Sites)
class SitesAdmin (admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Site)
class SiteAdmin (admin.ModelAdmin):
    list_display = ('site_id','date','a_value','b_value')
    #list_editable = ('date','a_value','b_value') # Make the item editable directly in the list

# Register your models here.
