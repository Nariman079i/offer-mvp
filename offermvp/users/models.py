from django.db.models import *
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .admin import *
from .services import *
class DefaultUser(AbstractBaseUser):
    
    email = EmailField(max_length=60, unique=True)
    
    date_joined = DateField(auto_now_add=True)
    last_login = DateField(auto_now=True)

    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = DefaultUserManager()

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

# Create your models here.
admin.site.register(DefaultUser)