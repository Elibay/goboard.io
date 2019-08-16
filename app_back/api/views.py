from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Player, PlayerToken, Lobby, Game, Participation
from api.serializers import ParticipationSerializer, PlayerSerializer, LobbySerializer


def get_player(request):
    return Player.objects.get(token=request.headers['Authorization'])


def kick_player(player):
    current_participation = player.participations.filter(is_current=True).first()
    if current_participation is not None:
        current_participation.is_current = False
        current_participation.save()


class RegisterAPIView(APIView):
    def get(self, request):
        new_player = Player.objects.create(nickname=request.data['nickname'])
        token = PlayerToken.objects.create(player=new_player)
        return Response(status=status.HTTP_200_OK, data={'token': token.key})


class GetPlayerInfoAPIView(APIView):
    def get(self, request):
        player = get_player(request)
        response = Response(status=status.HTTP_200_OK, data={})
        serializer = PlayerSerializer(player)
        response.data['nickname'] = serializer.data
        serializer = ParticipationSerializer(Participation.objects.filter(player=player), many=True)
        response.data['participations'] = serializer.data
        return response


class GetLobbyInfoAPIView(APIView):
    def get(self, request):
        player = get_player(request)
        lobby = Lobby.objects.get(id=request['lobby_id'])
        participation = player.participations.filter(lobby=lobby).first()
        if participation is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        response = Response(status=status.HTTP_200_OK, data={})
        response.data['lobby'] = LobbySerializer().data
        return response


class ChangeNameAPIView(APIView):
    def post(self, request):
        player = get_player(request)
        player.name = request.data['new_name']
        player.save()
        return Response(status=status.HTTP_200_OK)


class CreateLobbyAPIView(APIView):
    def post(self, request):
        player = get_player(request)
        kick_player(player)

        new_lobby = Lobby.objects.create(game=Game.objects.get(id=1))
        Participation.objects.create(lobby=new_lobby, player=player, is_current=True, is_admin=True)
        return Response(status=status.HTTP_200_OK, data={'lobby_id': new_lobby.id})


class JoinLobbyAPIView(APIView):
    def post(self, request):
        player = get_player(request)
        kick_player(player)

        lobby = Lobby.objects.get(id=request.data['lobby_id'])
        Participation.objects.create(lobby=lobby, player=player, is_current=True)
        return Response(status=status.HTTP_200_OK)


class LeaveLobbyAPIView(APIView):
    def post(self, request):
        player = get_player(request)
        kick_player(player)

        return Response(status=status.HTTP_200_OK)

