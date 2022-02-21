from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from.models import Title
from wrestler.models import Wrestler
from django.urls import reverse
from ppvs.models import PPV
from tag_teams.models import TagTeams

def index(request):
    all_titles_list= Title.objects.order_by('name')
    all_ppvs_list= PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")
    return render(request,"wrestler/titles_list.html",{"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})




def title_detail(request,title_id):

    try:
        t=Title.objects.get(id=title_id)
    except:
        raise Http404("Championship not found")
    if title_id==1:
        all_wrestlers_list = Wrestler.objects.order_by("-wwe_title_days", "-wwe_title_wins")

    elif title_id == 2:
        all_wrestlers_list = Wrestler.objects.order_by("-wh_title_days", "-wh_title_wins")
    elif title_id == 3:
        all_wrestlers_list = Wrestler.objects.order_by("-tag_title_days", "-tag_title_wins")
    elif title_id == 4:
        all_wrestlers_list = Wrestler.objects.order_by("-ic_title_days", "-ic_title_wins")
    elif title_id == 5:
        all_wrestlers_list = Wrestler.objects.order_by("-us_title_days", "-us_title_wins")
    elif title_id == 6:
        all_wrestlers_list = Wrestler.objects.order_by("-mitb")

    elif title_id == 7:
        all_wrestlers_list = Wrestler.objects.order_by("-kotr")
    elif title_id == 8:
        all_wrestlers_list = Wrestler.objects.order_by("-rr")
    elif title_id == 9:
        all_wrestlers_list = Wrestler.objects.order_by("-eu_title_days","-eu_title_wins")
    else:
        all_wrestlers_list = Wrestler.objects.order_by("-hc_title_days","-hc_title_wins")

    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")

    list_rank=[]
    for rank in range(1,len(all_wrestlers_list)+1):
        list_rank.append(rank)
    list_rank=set(list_rank)
    return render(request,"wrestler/title_detail.html",{"title":t,"all_wrestlers_list":all_wrestlers_list,"list_rank":list_rank,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})

def title_detail_name(request,title_id):

    try:
        t=Title.objects.get(id=title_id)
    except:
        raise Http404("Championship not found")
    all_wrestlers_list = Wrestler.objects.order_by("name")
    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")

    list_rank=[]
    for rank in range(1,len(all_wrestlers_list)+1):
        list_rank.append(rank)
    list_rank=set(list_rank)
    return render(request,"wrestler/title_detail.html",{"title":t,"all_wrestlers_list":all_wrestlers_list,"list_rank":list_rank,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})

def title_detail_name_down(request,title_id):

    try:
        t=Title.objects.get(id=title_id)
    except:
        raise Http404("Championship not found")
    all_wrestlers_list = Wrestler.objects.order_by("-name")
    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")

    list_rank=[]
    for rank in range(1,len(all_wrestlers_list)+1):
        list_rank.append(rank)
    list_rank=set(list_rank)
    return render(request,"wrestler/title_detail.html",{"title":t,"all_wrestlers_list":all_wrestlers_list,"list_rank":list_rank,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})

def title_detail_titles(request,title_id):

    try:
        t=Title.objects.get(id=title_id)
    except:
        raise Http404("Championship not found")
    if title_id==1:
        all_wrestlers_list = Wrestler.objects.order_by( "-wwe_title_wins","-wwe_title_days")

    elif title_id == 2:
        all_wrestlers_list = Wrestler.objects.order_by( "-wh_title_wins","-wh_title_days")
    elif title_id == 3:
        all_wrestlers_list = Wrestler.objects.order_by( "-tag_title_wins","-tag_title_days")
    elif title_id == 4:
        all_wrestlers_list = Wrestler.objects.order_by("-ic_title_wins","-ic_title_days")
    elif title_id == 5:
        all_wrestlers_list = Wrestler.objects.order_by( "-us_title_wins","-us_title_days")

    elif title_id == 9:
        all_wrestlers_list = Wrestler.objects.order_by("-eu_title_wins","-eu_title_days")
    elif title_id == 10:
        all_wrestlers_list = Wrestler.objects.order_by("-hc_title_wins","-hc_title_days")

    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")

    list_rank=[]
    for rank in range(1,len(all_wrestlers_list)+1):
        list_rank.append(rank)
    list_rank=set(list_rank)
    return render(request,"wrestler/title_detail.html",{"title":t,"all_wrestlers_list":all_wrestlers_list,"list_rank":list_rank,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})

def title_detail_titles_down(request,title_id):

    try:
        t=Title.objects.get(id=title_id)
    except:
        raise Http404("Championship not found")
    if title_id==1:
        all_wrestlers_list = Wrestler.objects.order_by( "wwe_title_wins","wwe_title_days")

    elif title_id == 2:
        all_wrestlers_list = Wrestler.objects.order_by( "wh_title_wins","wh_title_days")
    elif title_id == 3:
        all_wrestlers_list = Wrestler.objects.order_by( "tag_title_wins","tag_title_days")
    elif title_id == 4:
        all_wrestlers_list = Wrestler.objects.order_by("ic_title_wins","ic_title_days")
    elif title_id == 5:
        all_wrestlers_list = Wrestler.objects.order_by( "us_title_wins", "us_title_days")

    elif title_id == 9:
        all_wrestlers_list = Wrestler.objects.order_by("eu_title_wins", "eu_title_days")
    elif title_id == 10:
        all_wrestlers_list = Wrestler.objects.order_by("hc_title_wins","hc_title_days")

    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")

    list_rank=[]
    for rank in range(1,len(all_wrestlers_list)+1):
        list_rank.append(rank)
    list_rank=set(list_rank)
    return render(request,"wrestler/title_detail.html",{"title":t,"all_wrestlers_list":all_wrestlers_list,"list_rank":list_rank,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})


def title_detail_days_down(request,title_id):

    try:
        t=Title.objects.get(id=title_id)
    except:
        raise Http404("Championship not found")
    if title_id==1:
        all_wrestlers_list = Wrestler.objects.order_by( "wwe_title_days")

    elif title_id == 2:
        all_wrestlers_list = Wrestler.objects.order_by( "wh_title_days")
    elif title_id == 3:
        all_wrestlers_list = Wrestler.objects.order_by( "tag_title_days")
    elif title_id == 4:
        all_wrestlers_list = Wrestler.objects.order_by("ic_title_days")
    elif title_id == 5:
        all_wrestlers_list = Wrestler.objects.order_by( "us_title_days")

    elif title_id == 9:
        all_wrestlers_list = Wrestler.objects.order_by("eu_title_days")
    elif title_id == 10:
        all_wrestlers_list = Wrestler.objects.order_by("hc_title_days")

    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")

    list_rank=[]
    for rank in range(1,len(all_wrestlers_list)+1):
        list_rank.append(rank)
    list_rank=set(list_rank)
    return render(request,"wrestler/title_detail.html",{"title":t,"all_wrestlers_list":all_wrestlers_list,"list_rank":list_rank,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})