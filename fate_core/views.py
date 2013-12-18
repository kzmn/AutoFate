from rest_framework import viewsets
from fate_core.models import *
from fate_core.serializers import *

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class IssueViewSet(viewsets.ModelViewSet):
    model = Issue

class FaceViewSet(viewsets.ModelViewSet):
    model = Face

class PlaceViewSet(viewsets.ModelViewSet):
    model = Place

class SkillViewSet(viewsets.ModelViewSet):
    model = Skill