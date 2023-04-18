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
    pass


class PageSerializer(ModelSerializer):
    feedback = FeedBackSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'
