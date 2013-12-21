from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=128)
    setting = models.CharField(max_length=128)

    ## Dials
    ## TODO: Should this be a class
    number_of_aspects = models.IntegerField(default=5)
    number_of_phases = models.IntegerField(default=3)
    skill_cap = models.IntegerField(default=4)
    ## TODO: Skill shape enum
    ## TODO: Number of columns
    refresh_rate = models.IntegerField(default=3)
    initial_stunts = models.IntegerField(default=3)
    ## TODO: Stress tracks
    number_of_stress_boxes = models.IntegerField(default=2)
    ## TODO: Consequence slots


    def __str__(self):
        return self.name


class Aspect(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class Issue(Aspect):
    game = models.ForeignKey(Game)


class Face(Aspect):
    name = models.CharField(max_length=128)
    game = models.ForeignKey(Game)

    def __str__(self):
        return self.name


class Place(Aspect):
    name = models.CharField(max_length=128)
    game = models.ForeignKey(Game)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=128)
    game = models.ForeignKey(Game)

    def __str__(self):
        return self.name