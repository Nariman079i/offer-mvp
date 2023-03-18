from rest_framework.serializers import *
from .models import *


class StageSerializer(ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id','title', 'status')


class SaleSerializer(ModelSerializer):
    stage_id = StringRelatedField()

    class Meta:
        model = Sale
        fields = '__all__'


class SaleSerializerAdd(ModelSerializer):
    stage_id = IntegerField()

    class Meta:
        model = Sale
        fields = '__all__'