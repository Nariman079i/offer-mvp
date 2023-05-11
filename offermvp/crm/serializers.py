from rest_framework.serializers import *
from .models import *


class CRMServiceSeializer(ModelSerializer):
    img = HiddenField(default=None)

    class Meta:
        model = CRMService
        fields = "__all__"


class CRMSessionSeializer(ModelSerializer):
    class Meta:
        model = CRMSession
        fields = "__all__"


class CRMCustomerSeializer(ModelSerializer):
    class Meta:
        model = CRMCustomer
        fields = "__all__"


class CRMMasterSeializer(ModelSerializer):
    class Meta:
        model = CRMMaster
        fields = "__all__"


class StageSerializer(ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 'title', 'status')


class SaleSerializer(ModelSerializer):
    stage_id = StageSerializer()

    class Meta:
        model = Sale
        fields = '__all__'


class SaleSerializerAdd(ModelSerializer):
    stage_id = IntegerField()

    class Meta:
        model = Sale
        fields = '__all__'
