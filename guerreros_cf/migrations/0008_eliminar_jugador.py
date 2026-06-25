# Generated manually for guerreros_cf — elimina el modelo Jugador

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guerreros_cf', '0007_limpieza_y_biografia_director'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='jugador',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='equipo',
        ),
        migrations.DeleteModel(
            name='Jugador',
        ),
    ]
