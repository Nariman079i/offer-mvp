from django.contrib import admin
from django.contrib.auth.models import BaseUserManager


# Register your models here.
class DefaultUserManager(BaseUserManager):
    def create_user(self, email,password=None):

        if not email:
            raise ValueError("Обязательное поле")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("Oбязательное поле")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        return user
