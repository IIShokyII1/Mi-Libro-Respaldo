
from django import forms
from .models import  Alumno, Calificaciones, Profesor, Curso, AulaComun, ControlAsignatura, Anotacion, Apoderado, Comunicacion, asistencia
from django.contrib.admin.widgets import AdminDateWidget

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model= Profesor
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model= Curso
        fields = '__all__' 

class ProfesorForm(forms.ModelForm):
    class Meta:
        model= Profesor
        fields = '__all__'

class AulaForm(forms.ModelForm):
    class Meta:
        model = AulaComun
        fields = '__all__'
        widgets = {
          'registroAula': forms.Textarea(attrs={'rows':10, 'cols':50}),
        }
        
        

class ControlForm(forms.ModelForm):
    class Meta:
        model = ControlAsignatura
        fields = '__all__'
        widgets = { 
          'tareaAsignatura': forms.Textarea(attrs={'rows':6, 'cols':100}),
        }
        

class AnotacionForm(forms.ModelForm):
    class Meta:
        model= Anotacion
        fields = ['alumnos', 'profesor', 'asignatura', 'anotacion', 'tipo']
        widgets = {
            'anotacion': forms.Textarea(attrs={'rows':10, 'cols':70}),
        }

class ApoderadoForm(forms.ModelForm):
    class Meta:
        model = Apoderado
        fields = ['rut', 'nombres', 'apPaterno', 'apMaterno', 'fNacimiento', 'sexo', 'correo', 'alumno']

class ComunicacionForm(forms.ModelForm):
    class Meta:
        model = Comunicacion
        fields = ['name', 'subject', 'body', 'correo', 'status']
        widgets = {
            'body': forms.Textarea(attrs={ 'rows':10 , 'cols': 70}),
        }

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = ['alumno', 'asignatura', 'tipo', 'nota']
        widgets = {
            'nota': forms.TextInput(attrs={'size':'10'}),
        }

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = asistencia
        fields = ['alumnos', 'estado', 'justificacion']
        widgets = {
            'justificacion': forms.Textarea(attrs={ 'rows':3 , 'cols':30}),
        }
