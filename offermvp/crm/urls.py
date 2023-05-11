from django.urls import path, include
from .views import *
from rest_framework import routers
from django.views.decorators.cache import cache_page
from .views import *

router = routers.SimpleRouter()
router.register(r'customers', CRMCustomerAPIView)
router.register(r'sessions', CRMSessionAPIView)
router.register(r'masters', CRMMasterAPIView),
router.register(r'services', CRMServiceAPIView)
urlpatterns = [
    path('sales/', cache_page(60)(SaleListAPI.as_view())),
    path('sales/<int:pk>', SaleListAPI.as_view()),
    path('stages/', StageListAPI.as_view()),
    path('my_view/', MyView.as_view()),
    path('service/create/', ServiceCreateView.as_view()),
    path('mat/', AriphmeticOperations.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))

]
