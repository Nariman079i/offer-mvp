import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import  cache_page
from django.conf.urls.static import static

from offermvp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('crm/', include('crm.urls')),
    path('api/',include('salon.urls')),
    path('tatu/api/',include('tatu.urls'))
]
if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)),)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)