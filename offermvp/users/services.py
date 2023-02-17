from random import *
from smtplib import SMTPRecipientsRefused, SMTPDataError

from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.exceptions import ValidationError
from offermvp import settings


def generate_password(n=6):
    alph = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()'
    password = ''
    for i in range(n-n,n):
        password += choice(list(alph))
    return password


def send_mail_password(email:str,password:str):
    user = [email,]
    try:
        msg = render_to_string('email_verify/index.html', {'code': password})
        send_mail('Offer - Подтверждение аккаунта', msg, settings.EMAIL_HOST_USER, user, html_message=msg)
        return True
    except:
        return False

