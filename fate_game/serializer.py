from rest_framework import serializers
from fate_game.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'name', 'faces_and_places', 'number_of_aspects', 'number_of_phases', 'skill_cap', 'refresh_rate',
            'initial_stunts', 'number_of_stress_boxes', 'player_characters', 'faces_and_places')
