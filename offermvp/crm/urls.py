
from django.urls import path, include
from .views import *
from django.views.decorators.cache import  cache_page
from .views import *
urlpatterns = [
    path('sales/',cache_page(60)(SaleListAPI.as_view())),
    path('sales/<int:pk>', SaleListAPI.as_view()),
    path('stages/', StageListAPI.as_view())
]


