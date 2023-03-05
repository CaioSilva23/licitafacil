
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('summernote/', include('django_summernote.urls')),    
    path('admin/', admin.site.urls),
    path('', include('plataforma.urls')),
    path('email/', include('emails.urls')),
    path('clientes/', include('clientes.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)