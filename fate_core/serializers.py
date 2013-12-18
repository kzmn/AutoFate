from rest_framework import serializers
from fate_core.models import *

# Create serializers for models here.
class GameSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'setting', 'issue_set', 'face_set', 'place_set', 'skill_set')