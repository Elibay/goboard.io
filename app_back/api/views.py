import random

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from api.models import Player, Lobby, Game
from api.serializers import PlayerSerializer, LobbySerializer


class CreateLobbyAPIView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        token = ''
        for i in range(0, 20):
            token += chr(random.randint(0, 25) + ord('A'))
        new_lobby = Lobby.objects.create(game=Game.objects.get(id=1))
        new_player = Player.objects.create(name=request.data['name'], token=token, lobby=new_lobby, is_admin=True)
        new_player.save()
        return Response(
            status=status.HTTP_200_OK,
            data={
                'player': PlayerSerializer(new_player).data,
                'lobby': LobbySerializer(new_lobby).data,
            }
        )
