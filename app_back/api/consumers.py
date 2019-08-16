import json
from enum import Enum

from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import User


class WSConsumer(JsonWebsocketConsumer):

    class Methods(Enum):
        GET_LOBBY_INFO = 'get_lobby_info'

    # def __init__(self, *args, **kwargs):
    #     super(WSConsumer, self).__init__(*args, **kwargs)
    #
    #     self.player = None

    def connect(self):
        print('KEK')
        self.accept()
        # self.player = self.get_player_by_token()
        #
        # if self.player is None:
        #     self.accept()

    def receive(self, text_data, **kwargs):
        self.send(text_data="Hello world!")
        # data = text_data
        #
        # if 'method' not in data:
        #     return Responses.error('Method is not specified')
        #
        # params = data.get('params', {})
        #
        # if data['method'] == self.Methods.GET_LOBBY_INFO.value:
        #     ws_handler.get_lobby_info(data['params'], params.get(''))

    def disconnect(self, close_code):
        pass
