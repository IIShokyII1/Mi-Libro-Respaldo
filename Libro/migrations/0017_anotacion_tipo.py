# Generated by Django 3.2.5 on 2022-06-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0016_auto_20220629_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotacion',
            name='tipo',
            field=models.CharField(choices=[('---', '-----------'), ('Positiva', 'Positiva'), ('Negativa', 'Negativa')], default='---', max_length=20),
        ),
    ]