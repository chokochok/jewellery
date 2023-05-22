from django.contrib import admin
from django.urls import path, include
from mainapp.views import index, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('', include('userapp.urls')),
    path('', include('productapp.urls')),
    path('', index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
