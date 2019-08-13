import uuid
import random

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.
from api.models import Player, Lobby, Game, Participation

def reset_current_for_player(player):
    pass


class RegisterAPIView(APIView):
    def get(self, request=None):
        new_player = Player.objects.create(is_admin=False)
        token = Token.objects.get_or_create(user=new_player)
        return Response(status=status.HTTP_200_OK, data={'token': token.key})


class ChangeNameAPIView(APIView):
    def post(self, request):
        player = request.user
        player.name = request.data['new_name']
        player.save()
        return Response(status=status.HTTP_200_OK)


class JoinLobbyAPIView(APIView):
    def post(self, request):
        lobby = Lobby.objects.get(id=request.data['lobby_id'])
        Participation.objects.create(lobby=lobby, player=request.user, is_current=True)
        return Response(status=status.HTTP_200_OK)


class CreateLobbyAPIView(APIView):
    def post(self, request):
        new_lobby = Lobby.objects.create(game=Game.objects.get(id=1))
        Participation.objects.create(lobby=new_lobby, player=request.user, is_current=True, is_admin=True)
        return Response(status=status.HTTP_200_OK, data={'lobby_id': new_lobby.id})

