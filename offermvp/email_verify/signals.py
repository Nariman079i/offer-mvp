from django.db.models.signals import post_save
from django.dispatch import receiver
from email_verify.models import SMSManager

# @receiver(post_save,sender=SMSManager)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#

