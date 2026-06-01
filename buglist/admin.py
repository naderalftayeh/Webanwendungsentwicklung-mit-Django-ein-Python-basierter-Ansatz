
# Register your models here.
from django.contrib import admin
from .models import Bugs

class BugsAdmin(admin.ModelAdmin):
    list_display = ['melder','status','prio','kurzbeschreibung','datum']
    list_display_links = ['melder']
    list_editable = ['kurzbeschreibung','status']
    search_fields= ['melder']
    list_filter = ['melder','status']
admin.site.register(Bugs,BugsAdmin)
admin.site.site_header = 'Webtechnologien Project'
admin.site.site_title  ='Webtechnologien project'