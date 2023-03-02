
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import *
urlpatterns = [

    path('user/create/', UserCreateAPI.as_view()),
    path('user/list/',UserListAPI.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/token/verify/', UserVerifyAPI.as_view(), name='token_verify')
] 







