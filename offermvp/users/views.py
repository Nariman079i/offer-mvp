from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import *

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class UserCreateAPI(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserListAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user = DefaultUser.objects.all()
        serializer = UserCreateSerializer(user, many=True)

        return Response({'data': serializer.data})