# Generated by Django 3.2.5 on 2022-06-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=11)),
                ('nombres', models.CharField(max_length=60)),
                ('apPaterno', models.CharField(max_length=50)),
                ('apMaterno', models.CharField(max_length=50)),
                ('fNacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('N', 'Sin especificación'), ('F', 'Femenino'), ('M', 'Masculino')], default='N', max_length=1)),
                ('imagen', models.ImageField(null=True, upload_to='alumnos')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.CharField(max_length=100)),
            ],
        ),
    ]