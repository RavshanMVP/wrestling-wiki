from django.db import models

# Create your models here.

class TagTeams(models.Model):
    name = models.CharField("Name of tag team", max_length = 50)
    photo = models.TextField("Photo of tag team")
    main_page = models.TextField("Photo of tag team gor main page")
    stable = models.BooleanField("Is Stable?")
    members = models.TextField("Members of tag team")
    info = models.TextField("Info about tag team")
    gif1 = models.TextField("Moment")
    gif2 = models.TextField("Moment2")
    gif3 = models.TextField("Moment3")
    wwe_title_wins = models.IntegerField("Number of WWE championship wins")
    tag_title_wins = models.IntegerField("Number of tag team championship wins")
    ic_title_wins = models.IntegerField("Number of intercontinental championship wins")
    wh_title_wins = models.IntegerField("Number of World championship wins")
    us_title_wins = models.IntegerField("Number of United States championship wins")
    eu_title_wins = models.IntegerField("Number of European championship wins")
    hc_title_wins = models.IntegerField("Number of Hardcore championship wins")
    def __str__(self):
        return self.name