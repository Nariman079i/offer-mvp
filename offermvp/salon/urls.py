from django.urls import path
from salon.views import *

urlpatterns = [
    path('page/',MainPageAPI().as_view(),name="salon-page"),
    path('service/',ServiceAPI().as_view()),
    path('service/<int:id>',ServiceDetailAPI().as_view(),name="service-detail"),
    path('support/',SupportAPI().as_view())
]