from rest_framework import viewsets
from fate_game.models import *
from fate_game.serializer import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    model = Game
    serializer_class = GameSerializer
