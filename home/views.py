from django.shortcuts import render
from contact_form.models import ContactForm
from management_team.models import TeamMember
from slider.models import Slider
from roadmap.models import Roadmap
from ourfocus.models import Ourfocus
from marketing.models import News

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
    sliders = Slider.objects.filter()
    roadmaps = Roadmap.objects.filter()
    focuses = Ourfocus.objects.filter().order_by('id')
    news = News.objects.filter().order_by('id')
    context = {
        'core_team': core_team,
        'advisor_team': advisor_team,
        'partners': partners,
        'sliders': sliders,
        'yrs': list(range(2015, 2025)),
        'roadmaps':roadmaps,
        'focuses': focuses,
        'news': news,
    }
    return render(request, 'home/index.html', context)


            
        
        

