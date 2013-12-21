from django.db import models
from fate_game.models import Game
from fate_aspect.models import Aspect

# Create your models here.

class Character(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=128)
    description = models.TextField()
    refresh = models.IntegerField()
    aspects = models.ManyToManyField(Aspect)

    def __str__(self):
        return self.name