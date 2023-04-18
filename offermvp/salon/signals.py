from django.db.models.signals import post_save
from django.dispatch import receiver
from services import send_telegram_message
from .models import *

@receiver(post_save,sender=Support)
def create_profile(instance:Image, created, **kwargs):
    if created:
        message = f"{instance.name} {instance.message}"
        send_telegram_message(message)




