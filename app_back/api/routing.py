from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from api.consumers import WSConsumer


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "websocket": URLRouter([path('ws/', WSConsumer)]),
})
