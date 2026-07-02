from django.urls import path
from . import views

app_name = 'guerreros'

urlpatterns = [

    # INICIO
    path('', views.inicio, name='inicio'),

    # EQUIPOS (se conserva la vista y los datos; ya no aparece en el menú)
    path('equipos/', views.equipos_lista, name='equipos_lista'),
    path('equipos/<int:pk>/', views.equipo_detalle, name='equipo_detalle'),

    # NOTICIAS
    path('noticias/', views.noticias_lista, name='noticias_lista'),
    path('noticia/<slug:slug>/', views.noticia_detalle, name='noticia_detalle'),  # 👈 AQUÍ

    path('noticias/categoria/<str:categoria>/', views.noticias_categoria, name='noticias_categoria'),

    # LIGA
    path('liga/', views.liga_info, name='liga_info'),

    # STAFF
    path('directiva/', views.staff_lista, name='staff_lista'),

    # CONTACTO
    path('contacto/', views.contacto, name='contacto'),

    # API
    path('api/noticias/', views.api_noticias, name='api_noticias'),
]