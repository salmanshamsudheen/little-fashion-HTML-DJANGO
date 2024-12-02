from django.shortcuts import render
from .models import TeamMember

def team(request):
    team_members = TeamMember.objects.all().order_by('order_id')
    
    context = {
        'team_members' : team_members,
    }
    return render(request, 'about.html', context)


