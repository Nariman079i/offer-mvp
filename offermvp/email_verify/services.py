from django.core.mail import send_mail

from offermvp import settings


# def send_email_user(request,title,recipient,message):
#     send_mail(
#         title,
#         message,
#         settings.EMAIL_HOST_USER,
#         [recipient,]
# )