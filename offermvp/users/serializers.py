from rest_framework.serializers import *
from .models import *
from .services import generate_password ,send_mail_password
from email_verify import views
from rest_framework.exceptions import ValidationError
User = DefaultUser


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

    def create(self, validated_data):

        password = generate_password(8)
        if send_mail_password(email=validated_data["email"], password=password):
            user = User.objects.create_user(validated_data["email"],password=password)
        else:
            raise ValidationError({'email': "Введите валидную почту"})
        return user

