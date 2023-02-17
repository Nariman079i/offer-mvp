from random import randint

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework.views import APIView
from rest_framework.response import Response

class EmailVerify(APIView):
    def post(self,request):
        code = randint(100000, 999999)
        user = [request.data.get('recipient')]
        msg = render_to_string('email_confirmation/send.html', {'code': code})
        send_mail('Offer - Подтверждение аккаунта', msg, settings.EMAIL_HOST_USER, user, html_message=msg)
        return Response({'code':1})