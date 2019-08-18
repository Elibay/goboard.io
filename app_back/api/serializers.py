from rest_framework import serializers

from api.models import Player, Lobby, Participation


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'nickname', 'creation_time', 'user']


class ParticipationSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = Participation
        fields = ['id', 'lobby', 'player', 'is_admin', 'is_current']


class LobbySerializer(serializers.ModelSerializer):
    participants = ParticipationSerializer()

    class Meta:
        model = Lobby
        fields = '__all__'
