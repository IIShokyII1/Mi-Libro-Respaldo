import django_filters
from .models import *
from django import forms

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Calificaciones
        fields = '__all__'

class AsistenciaFilter(django_filters.FilterSet):
    class Meta:
        model = asistencia
        fields = ['estado']

class ControlFilter(django_filters.FilterSet):
    class Meta:
        model = ControlAsignatura
        fields = ['fecha_control']
        widgets = {
            "fecha_control": forms.SelectDateWidget()
        }

class AulaFilter(django_filters.FilterSet):
    class Meta:
        model = AulaComun
        fields = ['fecha_aula']

class AnotacionFilter(django_filters.FilterSet):
    class Meta:
        model = Anotacion
        fields = ['tipo']
