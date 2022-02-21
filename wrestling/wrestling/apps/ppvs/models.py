from django.db import models

# Create your models here.

class PPV(models.Model):
    main_name =models.CharField("Name of pay per view", max_length = 50)
    image =models.TextField("Image of pay per view")
    gif = models.TextField("GIFof pay per view", blank = True)
    wwe_title_matches = models.IntegerField("Number of wwe championship matches")
    wwe_title_changes = models.IntegerField("Number of wwe championship changes")

    wh_title_matches = models.IntegerField("Number of world heavyweight championship matches")
    wh_title_changes = models.IntegerField("Number of world heavyweight changes")

    tag_title_matches = models.IntegerField("Number of tag team championship matches")
    tag_title_changes = models.IntegerField("Number of tag team championship changes")

    ic_title_matches = models.IntegerField("Number of intercontinental championship matches")
    ic_title_changes = models.IntegerField("Number of intercontinental championship changes")

    us_title_matches = models.IntegerField("Number of united states championship matches")
    us_title_changes = models.IntegerField("Number of united states championship changes")



    def __str__(self):
        return self.main_name



class Titles(models.Model):
    title = models.CharField("Title that was defended", max_length = 50)
    image = models.TextField("Image")


    def __str__(self):
        return self.title


class Match(models.Model):
    result = models.TextField("Result of the match", )
    date = models.DateField("Date of the match")
    title = models.ForeignKey(Titles, on_delete =models.CASCADE)
    ppv = models.ForeignKey(PPV, on_delete = models.CASCADE)
    title_change = models.BooleanField("Title change?")

    def __str__(self):
        return self.result

