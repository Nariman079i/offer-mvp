from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models

# Create your models here.
class Messages(models.Model):
    message = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Send message to WebSocket
        # Получаем объект канала
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_room_1',
            {
                'type': 'chat_message',
                'message': {'id':self.pk ,'message':self.message }
            }
        )
