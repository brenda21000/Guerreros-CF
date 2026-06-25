from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Django
    path('admin/', admin.site.urls),

    # App Guerreros CF
    path('', include(('guerreros_cf.urls', 'guerreros'), namespace='guerreros')),
]

# Servir archivos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# ─────────────────────────────────────────
# ERROR 404 personalizado
# ─────────────────────────────────────────
handler404 = 'guerreros_cf.views.error_404'