from rest_framework import viewsets
from fate_character.models import *


class CharacterViewSet(viewsets.ModelViewSet):
    model = Character


class PlayerCharacterViewSet(viewsets.ModelViewSet):
    model = PlayerCharacter


class FaceOrPlaceCharacterViewSet(viewsets.ModelViewSet):
    model = FaceOrPlaceCharacter