# Generated manually for guerreros_cf — quita Equipo.entrenador, agrega año/fecha del logro

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guerreros_cf', '0008_eliminar_jugador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='entrenador',
        ),
        migrations.AddField(
            model_name='equipo',
            name='anio_logro',
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                help_text='Año en que se obtuvo el logro (ej. 2025)'
            ),
        ),
        migrations.AddField(
            model_name='equipo',
            name='fecha_logro',
            field=models.DateField(
                blank=True,
                null=True,
                help_text='Fecha exacta del logro (día/mes/año)'
            ),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='logo',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='equipos/logos/',
                help_text='Logo del equipo / foto del logro principal (ej. equipo levantando el trofeo)'
            ),
        ),
    ]
