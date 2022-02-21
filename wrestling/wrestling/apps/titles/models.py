from django.db import models

# Create your models here.

class Title(models.Model):
    name = models.CharField("Name of the championship",max_length = 100)
    image = models.TextField("Design of title", blank= True)
    info = models.TextField("Info about title",blank = True)
    gif = models.TextField("Gif", blank = True)
    def __str__(self):
        return self.name

