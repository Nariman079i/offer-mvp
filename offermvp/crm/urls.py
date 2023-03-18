
from django.urls import path, include
from .views import *

from .views import *
urlpatterns = [
    path('sales/', SaleListAPI.as_view()),
    path('sales/<int:pk>', SaleListAPI.as_view()),
    path('stages/', StageListAPI.as_view())
]


