from rest_framework.serializers import ModelSerializer

from chat.models import Messages


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = ('message','id')