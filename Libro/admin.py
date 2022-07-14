from django.contrib import admin

from Libro.models import Alumno, Asignatura, Calificaciones
from usuario.models import Usuario

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Asignatura)
admin.site.register(Calificaciones)
admin.site.register(Usuario)