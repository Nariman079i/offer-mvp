from rest_framework.response import Response
from rest_framework.views import APIView
from salon.serializers import *
from telebot import *


class MainPageAPI(APIView):
    def get(self,request):
        model = Page.objects.get(pk=1)
        serializer = PageSerializer(model,many=False,context={'request':self.request})

        return Response({
            'data':serializer.data
        })


class ServiceAPI(APIView):
    def get(self,request):
        type = self.request.query_params.get('type')
        m = Service.objects.all()
        if not type:
            serializer = ServiceSerializer(m,many=True,context={'request':self.request})
            return Response({
                'data': serializer.data
            })
        serializer = ServiceTitleSerializer(m, many=True, context={'request': self.request})
        return Response({
            'data': serializer.data
        })


class ServiceDetailAPI(APIView):
    def get(self,request,**kwargs):
        pk = kwargs.get('id')
        m = Service.objects.get(pk=pk)
        serializer = ServiceDetailSerializer(m,many=False,context={'request':self.request})
        return Response({
            'data': serializer.data
        })


class SupportAPI(APIView):
    def get(self,request):
        name = self.request.query_params.get('name')
        tel = self.request.query_params.get('tel')
        message = self.request.query_params.get('message')
        support = Support.objects.create(
            name=name,
            tel=tel,
            message=message
        )

        return Response({"ok":1})