from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from api.models.authorization import Player, MyToken
from api.models import Player, PlayerToken, Lobby, Game, Participation
from api.serializers import ParticipationSerializer, PlayerSerializer


def get_player(request):
    return Player.objects.get(token=request.headers['Authorization'])


def kick_player(player):
    current_participation = player.participations.get(is_current=True)
    if current_participation is not None:
        current_participation.is_current = False
        current_participation.save()


class RegisterAPIView(APIView):
    def get(self, request):
        new_player = Player.objects.create(username=request.data['username'])
        token = PlayerToken.objects.create(user=new_player)
        return Response(status=status.HTTP_200_OK, data={'token': token.key})


class GetPlayerInfoAPIView(APIView):
    def get(self, request):
        player = get_player(request)
        response = Response(status=status.HTTP_200_OK, data={})
        serializer = PlayerSerializer(player)
        response.data['username'] = serializer.data
        serializer = ParticipationSerializer(Participation.objects.filter(player=player), many=True)
        response.data['participations'] = serializer.data
        return response


class GetLobbyInfoAPIView(APIView):
    def get(self, requset):
        lobby = Lobby.objects.get(id=requset['lobby_id'])
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

