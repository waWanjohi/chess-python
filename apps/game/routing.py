from django.urls import re_path

from apps.game.consumers import MovesConsumer



websocket_urlpatterns = [
    re_path("ws/play/$", MovesConsumer.as_asgi()),
]
