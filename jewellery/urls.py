from django.contrib import admin
from django.urls import path, include
from mainapp.views import index, about
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('', include('userapp.urls')),
    path('', include('productapp.urls')),
    path('', index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
