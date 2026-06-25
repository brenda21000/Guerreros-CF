# Generated manually for guerreros_cf — precarga anuncios visuales (flyers de equipos/eventos)

from django.db import migrations


ANUNCIOS = [
    {
        'nombre_patrocinador': 'Liga Guerreros Femenil Yauhquemehcan',
        'imagen': 'anuncios/liga_femenil_yauhquemehcan.jpeg',
        'division': 'femenil',
        'orden': 4,
    },
    {
        'nombre_patrocinador': 'Equipo Pinponas — Femenil Libre',
        'imagen': 'anuncios/equipo_pinponas_femenil.png',
        'division': 'femenil',
        'orden': 5,
    },
    {
        'nombre_patrocinador': 'Academia Guerreros — Campeón Nacional Femenil Libre',
        'imagen': 'anuncios/academia_campeon_femenil.png',
        'division': 'femenil',
        'orden': 6,
    },
    {
        'nombre_patrocinador': 'Equipo Juventus — Categoría Libre',
        'imagen': 'anuncios/equipo_juventus_varonil.png',
        'division': 'varonil',
        'orden': 4,
    },
    {
        'nombre_patrocinador': 'Equipo Monaguillos — Categoría Libre',
        'imagen': 'anuncios/equipo_monaguillos_varonil.png',
        'division': 'varonil',
        'orden': 5,
    },
    {
        'nombre_patrocinador': 'Liga Guerreros Yauhquemehcan (Varonil y Juvenil)',
        'imagen': 'anuncios/liga_guerreros_general.jpeg',
        'division': 'todas',
        'orden': 7,
    },
]


def crear_anuncios(apps, schema_editor):
    Anuncio = apps.get_model('guerreros_cf', 'Anuncio')
    for datos in ANUNCIOS:
        Anuncio.objects.get_or_create(
            nombre_patrocinador=datos['nombre_patrocinador'],
            defaults={
                'imagen': datos['imagen'],
                'division': datos['division'],
                'orden': datos['orden'],
                'activo': True,
            }
        )


def eliminar_anuncios(apps, schema_editor):
    Anuncio = apps.get_model('guerreros_cf', 'Anuncio')
    nombres = [d['nombre_patrocinador'] for d in ANUNCIOS]
    Anuncio.objects.filter(nombre_patrocinador__in=nombres).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('guerreros_cf', '0005_anuncio'),
    ]

    operations = [
        migrations.RunPython(crear_anuncios, eliminar_anuncios),
    ]
