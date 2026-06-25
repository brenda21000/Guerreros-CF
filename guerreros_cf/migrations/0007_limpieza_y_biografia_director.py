# Generated manually for guerreros_cf — limpieza de modelos y biografía de director

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guerreros_cf', '0006_precargar_anuncios_flyers'),
    ]

    operations = [
        # ── Eliminar Partido (y su FK arbitro hacia Staff) ──
        migrations.RemoveField(
            model_name='partido',
            name='arbitro',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='equipo_local',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='equipo_visitante',
        ),
        migrations.DeleteModel(
            name='Partido',
        ),

        # ── Eliminar Inscripcion ──
        migrations.DeleteModel(
            name='Inscripcion',
        ),

        # ── Equipo: agregar descripción de logros ──
        migrations.AddField(
            model_name='equipo',
            name='descripcion_logros',
            field=models.TextField(
                blank=True,
                help_text='Ej: Campeón Nacional Femenil Libre 2025, Subcampeón Liga Juvenil 2024...'
            ),
        ),

        # ── Staff: ampliar a biografía completa de director ──
        migrations.AlterField(
            model_name='staff',
            name='cargo',
            field=models.CharField(
                choices=[
                    ('director', 'Director General'),
                    ('tecnico', 'Director Técnico'),
                    ('secretaria', 'Secretaria General'),
                    ('arbitro', 'Coordinador de Árbitros'),
                    ('cancha', 'Encargado de Cancha'),
                    ('tesorera', 'Tesorera'),
                    ('otro', 'Otro'),
                ],
                default='director',
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name='staff',
            name='bio',
            field=models.TextField(
                blank=True,
                help_text='Biografía completa: trayectoria, experiencia, visión de la liga, logros, etc.'
            ),
        ),
        migrations.AddField(
            model_name='staff',
            name='anios_experiencia',
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                help_text='Años de experiencia dirigiendo la liga o en el fútbol'
            ),
        ),
        migrations.AddField(
            model_name='staff',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=20),
        ),

        # ── Nuevo modelo: galería de fotos del Staff/Director ──
        migrations.CreateModel(
            name='StaffImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='staff/galeria/')),
                ('descripcion', models.CharField(blank=True, max_length=200)),
                ('staff', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='galeria',
                    to='guerreros_cf.staff',
                )),
            ],
        ),
    ]
