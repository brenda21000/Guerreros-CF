# Generated manually for guerreros_cf — agrega campo Equipo.entrenador y modelo Trofeo

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guerreros_cf', '0003_alter_equipo_options_remove_equipo_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='entrenador',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='equipos_entrenados',
                to='guerreros_cf.staff',
            ),
        ),
        migrations.CreateModel(
            name='Trofeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_torneo', models.CharField(max_length=150)),
                ('anio', models.PositiveSmallIntegerField()),
                ('equipo', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='trofeos',
                    to='guerreros_cf.equipo',
                )),
            ],
            options={
                'ordering': ['-anio'],
            },
        ),
    ]
