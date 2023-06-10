from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apiv2 import settings

urlpatterns = [
    path('dadybro/', admin.site.urls),
    path('api/v2/', include('ilans.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)