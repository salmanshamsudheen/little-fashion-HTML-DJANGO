from django.contrib import admin
from .models import TeamMember

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    
admin.site.register(TeamMember, TeamMemberAdmin)    
