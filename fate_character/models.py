from django.db import models
from fate_core.models import Game

# Create your models here.

class Character(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=128)
