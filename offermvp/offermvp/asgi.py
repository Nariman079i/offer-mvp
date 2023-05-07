from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.wsgi import get_wsgi_application
from django.urls import path
from crm import consumers

websocket_urlpatterns = [
    path('ws/<int:pk>/', consumers.MyConsumer),
]

application = ProtocolTypeRouter({
    "http":get_wsgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),
})