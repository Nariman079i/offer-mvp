from django.urls import path
from .views import *

urlpatterns = [
    path('page/',MainPageAPI().as_view()),
]