# Generated by Django 3.2.5 on 2022-06-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0009_alter_calificaciones_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicacion',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
