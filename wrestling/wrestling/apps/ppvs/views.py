from django.shortcuts import render
from django.http import Http404
from .models import PPV, Match, Titles
from titles.models import Title
from tag_teams.models import TagTeams

# Create your views here.
def index(request):
    all_ppvs_list = PPV.objects.order_by("id")
    all_titles_list = Title.objects.order_by("name")
    all_tag_teams_list = TagTeams.objects.order_by("name")
    return render(request, "wrestler/ppv_list.html", {"all_ppvs_list": all_ppvs_list,"all_titles_list":all_titles_list,"all_tag_teams_list":all_tag_teams_list})


def detail(request, ppv_id):
    try:
        p = PPV.objects.get(id=ppv_id)
    except:
        raise Http404("PPV NOT FOUND")

    all_titles_list = Titles.objects.order_by("id")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")
    return render(request, "wrestler/ppv_detail.html", {"PPV": p, "all_titles_list": all_titles_list,"all_ppvs_list":all_ppvs_list,"all_tag_teams_list":all_tag_teams_list})


def title_detail(request, ppv_id, title_id):
    try:
        t = Titles.objects.get(id=title_id )
        p = PPV.objects.get(id=ppv_id)


    except:
        raise Http404("PPV NOT FOUND")

    all_matches_list = Match.objects.order_by("date")
    all_titles_list = Title.objects.order_by("id")
    all_ppvs_list = PPV.objects.order_by("id")
    all_tag_teams_list = TagTeams.objects.order_by("name")



    return render(request, "wrestler/ppv_title_detail.html",
                  {"PPV": p, "TITLE": t, "all_matches_list": all_matches_list, "all_titles_list": all_titles_list,
                   "all_ppvs_list": all_ppvs_list,  "all_tag_teams_list":all_tag_teams_list})
