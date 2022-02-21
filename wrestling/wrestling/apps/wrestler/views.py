from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from.models import Wrestler
from titles.models import Title
from ppvs.models import PPV
from tag_teams.models import TagTeams
# Create your views here.

def index(request):
    all_wrestlers_list = Wrestler.objects.order_by("name")
    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")
    return render(request,"wrestler/list.html",{"all_wrestlers_list":all_wrestlers_list,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})



def detail(request, wrestler_id):
    try:
        w=Wrestler.objects.get(id=wrestler_id)
    except:
        raise Http404("Wrestler not found")
    all_wrestlers_list = Wrestler.objects.order_by("name")
    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")

    titles = Title.objects.order_by("id")
    titles = titles[:5]
    wwe = Title.objects.get(id=1)
    wh = Title.objects.get(id=2)

    tag = Title.objects.get(id=3)
    ic = Title.objects.get(id=4)
    us = Title.objects.get(id=5)

    mitb = Title.objects.get(id=6)
    kotr = Title.objects.get(id=7)
    rr = Title.objects.get(id=8)

    eu = Title.objects.get(id =9)
    hc = Title.objects.get(id=10)


    return render(request,"wrestler/detail.html",{"wrestler":w,"titles":titles,"mitb":mitb,"kotr":kotr,"rr":rr,"wwe":wwe,"wh":wh,"tag":tag,"ic":ic,"us":us,"all_wrestlers_list":all_wrestlers_list,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list,"eu":eu,"hc":hc})
