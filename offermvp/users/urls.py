
from django.urls import path, include

from .views import *
urlpatterns = [

    path('user/create/', UserCreateAPI.as_view()),
    path('user/list/',UserListAPI.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
] 

