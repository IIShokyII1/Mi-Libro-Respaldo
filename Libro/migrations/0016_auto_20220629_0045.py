# Generated by Django 3.2.5 on 2022-06-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0015_alter_asistencia_alumnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='aulacomun',
            name='asuntoAulaComun',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='controlasignatura',
            name='asuntoControlasig',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
