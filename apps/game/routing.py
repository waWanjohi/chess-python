from django.urls import re_path

from apps.game.consumers import MovesConsumer

# re_path(r'ws/play/(?P<game_id>\w+)/$', MovesConsumer.as_asgi()),

websocket_urlpatterns = [
    re_path("ws/play/$", MovesConsumer.as_asgi()),
]
