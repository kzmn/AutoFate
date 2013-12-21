from rest_framework import viewsets
from fate_game.models import *


class GameViewSet(viewsets.ModelViewSet):
    model = Game
