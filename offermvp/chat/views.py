from django.http import HttpResponse
from django.shortcuts import render
from .models import Messages
from rest_framework.views import APIView
from .serializers import MessageSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class AddMessageAPI(ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Messages.objects.all()