# Generated by Django 3.2.5 on 2022-06-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0006_calificaciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calificaciones',
            old_name='notas',
            new_name='tipo',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='nota',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]