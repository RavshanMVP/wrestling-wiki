from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404, HttpResponse
from .models import TagTeams
from wrestler.models import Wrestler
from titles.models import Title
from ppvs.models import PPV
#
# # Create your views here.
def tag_index(request):
    all_tag_teams_list = TagTeams.objects.order_by("name")
    all_wrestlers_list = Wrestler.objects.order_by("name")
    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")
    return render(request,"wrestler/tag_list.html",{"all_tag_teams_list" :all_tag_teams_list,"all_wrestlers_list":all_wrestlers_list,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list })

def tag_detail(request, tag_id):
    try:
        tt = TagTeams.objects.get(id = tag_id)
    except:
        raise Http404("Tag team not not found")

    all_tag_teams_list = TagTeams.objects.order_by("name")
    all_wrestlers_list = Wrestler.objects.order_by("name")
    all_titles_list = Title.objects.order_by("name")
    all_ppvs_list = PPV.objects.order_by("id")



    return render(request,"wrestler/tag_detail.html",{"all_tag_teams_list" :all_tag_teams_list,"all_wrestlers_list":all_wrestlers_list,"all_titles_list":all_titles_list,"all_ppvs_list":all_ppvs_list ,"tt":tt})