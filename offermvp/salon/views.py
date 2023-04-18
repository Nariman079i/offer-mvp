from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from telebot import *



class MainPageAPI(APIView):
    def get(self,request):
        model = Page.objects.get(pk=1)
        serializer = PageSerializer(model,many=False)

        return Response({
            'data':serializer.data
        })

class SupportAPI(APIView):
    def get(self,request):
        Support.objects.create(**self.request.query_params)
        return Response({"ok":1})