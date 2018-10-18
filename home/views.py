from django.shortcuts import render
from contact_form.models import ContactForm
from management_team.models import TeamMember

def create_groups(members):
    group_list = []
    group_section = []
    index = 0
    for member in members:
        index = index + 1
        group_section.append(member)
        if index % 3 == 0:
            group_list.append(group_section)
            group_section = []
    
    if index % 3 != 0:
        group_list.append(group_section)
    
    return group_list

def index(request):
    core_team = create_groups(TeamMember.objects.filter(team='Core'))
    advisor_team = create_groups(TeamMember.objects.filter(team='Advisor'))
    partners = create_groups(TeamMember.objects.filter(team='Partner'))
    context = {
        'core_team': core_team,
        'advisor_team': advisor_team,
        'partners': partners
    }
    return render(request, 'home/index.html', context)


            
        
        

