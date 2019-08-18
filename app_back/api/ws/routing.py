from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import LobbyConsumer


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "websocket": URLRouter([path('lobby/', LobbyConsumer)]),
})
