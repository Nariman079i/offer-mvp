from django.urls import path
from tatu.views import *

urlpatterns = [
    path('page/',MainPageAPI().as_view(),name='tatu-page'),
    path('service/',ServiceAPI().as_view()),
    path('service/<int:id>/',ServiceDetailAPI.as_view(),name='servicetatu-detail'),
    path('support/',SupportAPI().as_view())
]