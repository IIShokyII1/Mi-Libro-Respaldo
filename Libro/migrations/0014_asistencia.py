# Generated by Django 3.2.5 on 2022-06-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0013_auto_20220627_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumnos', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_asistencia', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('Presente', 'Presente'), ('Ausente', 'Ausente'), ('Justificado', 'Justificado')], default='Presente', max_length=13)),
                ('justificacion', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-fecha_asistencia',),
            },
        ),
    ]
