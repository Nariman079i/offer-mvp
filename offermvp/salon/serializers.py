from rest_framework.serializers import *
from .models import *

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
class FeedBackSerializer(ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'


class ServicePriceSerializer(ModelSerializer):
    class Meta:
        model = ServicePrice
        fields = '__all__'



class ServiceSerializer(HyperlinkedModelSerializer):
    images = ImageSerializer(many=True)
    # hyper = HyperlinkedIdentityField(view_name='service-detail',many=False)
    class Meta:
        model = Service
        fields = ('title','direct_description','images','url')
        extra_kwargs = {
                    'url': {'lookup_field': 'id'}
                }
class PageSerializer(ModelSerializer):
    feedback = FeedBackSerializer(many=True)
    service_list = ServiceSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'
