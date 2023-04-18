from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class MainPageAPI(APIView):
    def get(self,request):
        model = Page.objects.get(pk=1)
        serializer = PageSerializer(model,many=False)

        return Response({
            'data':serializer.data
        })