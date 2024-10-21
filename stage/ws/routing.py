from .consumers import StageConsumer
from django.urls import path

ws_urlpatterns = [
    path('ws/stage/<uuid:stage_id>/',StageConsumer.as_asgi()),
]