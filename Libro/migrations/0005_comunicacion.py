# Generated by Django 3.2.5 on 2022-06-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0004_apoderado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('N', '------------'), ('Editando', 'Editando'), ('Publicado', 'Publicado')], default='N', max_length=10)),
                ('correo', models.ManyToManyField(to='Libro.Apoderado')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
