from rest_framework.serializers import *
from .models import *


class FeedBackSerializer(ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'


class ServicePriceSerializer(ModelSerializer):
    class Meta:
        model = ServicePrice
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class PageSerializer(ModelSerializer):
    feedback = FeedBackSerializer(many=True)
    service_list = ServiceSerializer(many=True)
    class Meta:
        model = Page
        fields = '__all__'