from django.shortcuts import render
from rest_framework.views import *
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny


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
