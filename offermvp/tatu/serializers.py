from rest_framework.serializers import *
from tatu.models import *


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
        model = ServiceTatu
        fields = '__all__'


class ServiceTatuSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ServiceTatu
        fields = ('id','title', 'direct_description', 'url', 'img')
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }


class ServiceTitleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ServiceTatu
        fields = ('title', 'url')
        extra_kwargs = {
            'url':{'lookup_field':'id'}
        }


class PageSerializer(ModelSerializer):
    feedback = FeedBackSerializer(many=True)
    service_list = ServiceTatuSerializer(many=True)
    image_list = ImageSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'

