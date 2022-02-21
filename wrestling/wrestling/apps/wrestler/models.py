from django.db import models

# Create your models here.

class Wrestler(models.Model):
    name = models.CharField("Name of wrestler",max_length=50)
    wwe_title_wins = models.IntegerField("Number of WWE championship wins")
    tag_title_wins = models.IntegerField("Number of tag team championship wins")
    ic_title_wins = models.IntegerField("Number of intercontinental championship wins")
    wh_title_wins = models.IntegerField("Number of World championship wins")
    us_title_wins = models.IntegerField("Number of United States championship wins")
    eu_title_wins = models.IntegerField("Number og European Championship wins")
    hc_title_wins = models.IntegerField("Number of Hardcore Championship wins")
    info =models.TextField("Brief info about wrestler")

    mitb = models.TextField("Money in the bank contract wins",blank=True)
    cash_in =models.TextField("Money in the bank cash in",blank=True)
    kotr = models.TextField("King of the ring tournament wins",blank=True)
    rr = models.TextField("Royal Rumble Wins",blank=True)
    rr_wm = models.TextField("Royal Rumble winner at Wrestlemania", blank=True)

    photo = models.TextField("Photo of wrestler")
    main_page=models.TextField("Photo of wrestler for main page")
    finisher =models.TextField("Finisher of wrestler", blank = True)
    finisher2 = models.TextField("Finisher of wrestler 2", blank=True)
    finisher3 = models.TextField("Finisher of wrestler 3", blank=True)

    wwe_title_days = models.IntegerField("Days WWE championship was held")
    tag_title_days = models.IntegerField("Days tag team championship was held")
    ic_title_days = models.IntegerField("Days intercontinental championship was held")
    wh_title_days = models.IntegerField("Days world championship was held")
    us_title_days = models.IntegerField("Days United States championship was held")
    eu_title_days = models.IntegerField("Days European championship was held",)
    hc_title_days = models.IntegerField("Days Hardcore championship was held")

    tag_teams = models.TextField("Tag teams or stable wrestler was a part of", blank = True)
    tag_teams2 = models.TextField("Tag teams or stable wrestler was a part of", blank=True)
    tag_teams3 = models.TextField("Tag teams or stable wrestler was a part of", blank=True)
    tag_teams4 = models.TextField("Tag teams or stable wrestler was a part of", blank=True)
    tag_teams5 = models.TextField("Tag teams or stable wrestler was a part of", blank=True)
    tag_teams6 = models.TextField("Tag teams or stable wrestler was a part of", blank=True)
    def __str__(self):
        return self.name

