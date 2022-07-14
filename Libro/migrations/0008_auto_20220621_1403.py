# Generated by Django 3.2.5 on 2022-06-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0007_auto_20220621_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='nota',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='calificaciones',
            name='tipo',
            field=models.CharField(choices=[('-', '-----'), ('N1', 'N°1'), ('N2', 'N°2'), ('N3', 'N°3'), ('N4', 'N°4'), ('N5', 'N°5'), ('N6', 'N°6'), ('N7', 'N°7')], default='-', max_length=15),
        ),
    ]