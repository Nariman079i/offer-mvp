from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from crm import consumers

websocket_urlpatterns = [
    path('ws/<int:pk>/', consumers.MyConsumer),
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
})