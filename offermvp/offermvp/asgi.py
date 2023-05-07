from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from crm import consumers

websocket_urlpatterns = [
    path('ws/<int:pk>/', consumers.MyConsumer),
]

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),
})