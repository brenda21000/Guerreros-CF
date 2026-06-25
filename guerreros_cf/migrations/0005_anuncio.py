# Generated manually for guerreros_cf — agrega modelo Anuncio (publicidad/patrocinadores)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guerreros_cf', '0004_equipo_entrenador_trofeo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_patrocinador', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to='anuncios/')),
                ('link', models.URLField(blank=True)),
                ('division', models.CharField(
                    choices=[
                        ('todas', 'Todas las divisiones'),
                        ('femenil', 'Femenil'),
                        ('juvenil', 'Juvenil'),
                        ('varonil', 'Varonil'),
                    ],
                    default='todas',
                    max_length=20,
                )),
                ('activo', models.BooleanField(default=True)),
                ('orden', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['orden', '-id'],
            },
        ),
    ]
