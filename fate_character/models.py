from django.db import models
from fate_aspect.models import Aspect
from fate_game.models import Game


class Character(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    refresh = models.IntegerField()
    aspects = models.ManyToManyField(Aspect)

    def __str__(self):
        return self.name


class PlayerCharacter(Character):
    game = models.ForeignKey(Game, related_name='player_characters')


class FaceOrPlaceCharacter(Character):
    game = models.ForeignKey(Game, related_name='faces_and_places')