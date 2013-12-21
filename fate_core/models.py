from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=128)
    setting = models.CharField(max_length=128)

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