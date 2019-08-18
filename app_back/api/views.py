from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Player, Lobby, Game, Participation
from api.serializers import ParticipationSerializer, PlayerSerializer, LobbySerializer


def authorize_player(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            player = Player.objects.get(token=request.headers['Authorization'].split(' ')[1])
        except (Player.DoesNotExist, KeyError, IndexError):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        setattr(request, 'player', player)
        return func(self, request, *args, **kwargs)
    return wrapper


def kick_player(player):
    try:
        current_participation = player.participations.get(is_current=True)
    except Participation.DoesNotExist:
        return

    current_participation.is_current = False
    if current_participation.is_admin:
        current_participation.is_admin = False
        next_admin = current_participation.lobby.participants.filter(is_current=True).order_by('time_joined').first()
        if next_admin is not None:
            next_admin.is_admin = True
            next_admin.save()

    current_participation.save()


class RegisterAPIView(APIView):
    def get(self, request):
        player = Player.objects.create(nickname=request.data['nickname'])
        return Response(status=status.HTTP_200_OK, data={'token': player.token, 'id': player.id})


class ChangeNicknameAPIView(APIView):
    @authorize_player
    def post(self, request):
        request.player.nickname = request.data['new_nickname']
        request.player.save()
        return Response(status=status.HTTP_200_OK)


class CreateLobbyAPIView(APIView):
    @authorize_player
    def post(self, request):
        kick_player(request.player)
        new_lobby = Lobby.objects.create(game=Game.objects.get(id=request.data['game_id']))
        Participation.objects.create(lobby=new_lobby, player=request.player, is_current=True, is_admin=True)
        return Response(status=status.HTTP_200_OK, data={'lobby_id': new_lobby.id})


class JoinLobbyAPIView(APIView):
    @authorize_player
    def post(self, request):
        try:
            lobby = Lobby.objects.get(id=request.data['lobby_id'])
        except Lobby.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        kick_player(request.player)
        Participation.objects.create(lobby=lobby, player=request.player, is_current=True)
        return Response(status=status.HTTP_200_OK)


class LeaveLobbyAPIView(APIView):
    @authorize_player
    def post(self, request):
        kick_player(request.player)
        return Response(status=status.HTTP_200_OK)


class GetPlayerInfoAPIView(APIView):
    def get(self, request):
        player = Player.objects.get(id=request.data['player_id'])
        response = Response(status=status.HTTP_200_OK, data={})
        serializer = PlayerSerializer(player)
        response.data['player'] = serializer.data
        serializer = ParticipationSerializer(Participation.objects.filter(player=player), many=True)
        response.data['participations'] = serializer.data
        return response


class GetLobbyInfoAPIView(APIView):
    def get(self, request):
        lobby = Lobby.objects.get(id=request['lobby_id'])
        return Response(status=status.HTTP_200_OK, data={'lobby': LobbySerializer(lobby).data})
