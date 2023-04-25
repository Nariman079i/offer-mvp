from rest_framework.serializers import *
from .models import *


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('img',)


class FeedBackSerializer(ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'


class ServicePriceSerializer(ModelSerializer):
    class Meta:
        model = ServicePrice
        fields = '__all__'


class ServiceDetailSerializer(ModelSerializer):
    images = ImageSerializer(many=True)
    price_list = ServicePriceSerializer(many=True)

    class Meta:
        model = Service
        fields = '__all__'


class ServiceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'direct_description', 'url', 'img')
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }


class ServiceTitleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'url')
        extra_kwargs = {
            'url':{'lookup_field':'id'}
        }


class PageSerializer(ModelSerializer):
    feedback = FeedBackSerializer(many=True)
    service_list = ServiceSerializer(many=True)
    image_list = ImageSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'




