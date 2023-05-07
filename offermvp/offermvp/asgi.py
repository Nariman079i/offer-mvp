from asgiref.sync import async_to_sync
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

from crm.consumers import MyConsumer

websocket_urlpatterns = [
    path('ws/<int:pk>/', async_to_sync(MyConsumer)),
]



django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': URLRouter(websocket_urlpatterns)
})