from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.permissions import AllowAny
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.generic import View
from django.http import HttpResponse

class CRMCustomerAPIView(ModelViewSet):
    serializer_class = CRMCustomerSeializer
    queryset = CRMCustomer.objects.all()


class CRMServiceAPIView(ModelViewSet):
    serializer_class = CRMServiceSeializer
    queryset = CRMService.objects.all()


class CRMSessionAPIView(ModelViewSet):
    serializer_class = CRMSessionSeializer
    queryset = CRMSession.objects.all()


class CRMMasterAPIView(ModelViewSet):
    serializer_class = CRMMasterSeializer
    queryset = CRMMaster.objects.all()

class MyView(View):
    def get(self, request):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "my_group",
            {
                "type": "send_message",
                "message": "Hello, world!"
            }
        )
        return HttpResponse("OK")

class SaleListAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            sales = Sale.objects.all()
            serializer = SaleSerializer(sales, many=True)
            return Response(serializer.data)
        sales = Sale.objects.filter(pk=pk)
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data[0])

    def post(self, request):
        serializer = SaleSerializerAdd(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"data": f"Not objects with pk = {pk}"})

        try:
            instance = Sale.objects.get(pk=pk)
        except:
            return Response({"data": f"Not objects with pk = {pk}"})

        serializer = SaleSerializerAdd(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        sale = Sale.objects.filter(pk=pk).delete()

        return Response({'data': "Deleted success!"})


class StageListAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        stage = Stage.objects.all()
        serializer = StageSerializer(stage, many=True)

        return Response(serializer.data)

class ServiceCreateView(APIView):
    def post(self,request):
        m = CRMService.objects.create(**request.data)
        serializer = CRMServiceSeializer(m,many=False)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_room_1',
            {
                'type': 'chat_message',
                'message': serializer.data
            }
        )
        return Response({'data':serializer.data})

class AriphmeticOperations(APIView):
    def get(self,request):
        output = 0
        data = {
            'data':output
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_room_1',
            {
                'type': 'chat_message',
                'message': data
            }
        )
        return Response(data)
