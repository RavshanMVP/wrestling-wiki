from django.shortcuts import render
from wrestler.models import Wrestler
from titles.models import Title
from ppvs.models import PPV
from tag_teams.models import TagTeams

# Create your views here.
def main_page_index(request):
    some_wrestlers_list = Wrestler.objects.order_by("id")
    some_wrestlers_list= some_wrestlers_list[:7]
    all_wrestlers_list = Wrestler.objects.order_by("name")

    all_titles_list = Title.objects.order_by("id")
    some_titles_list = all_titles_list[:5]
    all_ppvs_list = PPV.objects.order_by("id")
    some_ppvs_list = all_ppvs_list[:4]
    all_tag_teams_list = TagTeams.objects.order_by("id")
    some_tag_teams_list = all_tag_teams_list[:5]
    return render(request,"wrestler/main_page.html",{"some_wrestlers_list":some_wrestlers_list,"all_wrestlers_list":all_wrestlers_list,"some_titles_list":some_titles_list,"some_ppvs_list":some_ppvs_list,"some_tag_teams_list":some_tag_teams_list,"all_ppvs_list":all_ppvs_list,"all_titles_list":all_titles_list,"all_tag_teams_list":all_tag_teams_list})