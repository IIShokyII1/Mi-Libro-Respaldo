from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (AgregarNota, Cursos, admin, agregar_Alumno, detalleAnotacion, detalleControlAsig, listAlumno, modAlumno, eliminarAlumno, agregar_Profesor,listProf,modProf,eliminarProfesor, agregarCurso,
                    listCurso, modCursos,eliminarCurso, agregar_anotacion, anotaciones, lista_anotaciones, modAnotacion, eliminarAnotacion, agregarAulaComun, listAulaComun,
                    modAula, eliminarAulaComun, agregarControlAsig, listControlAsig, modControl, eliminarControlAsig, agregar_Apoderado, comunicaciones, nuevoCorreo, 
                    detalleCorreo, perfil, updateCorreo, eliminarCorreo, calificaciones, Notas, Home, Asistencia, tomaAsistencia, listar_Apoderados, modApoderados, eliminarApoderado, allAsistencia, modAsistecia,
                    detalleAulaComun)
urlpatterns = [
    path('Administracion/', login_required(admin), name= 'admin'),
    path('Perfil/', login_required(perfil), name='perfil'),

    path('agregar_Alumno/', agregar_Alumno, name='agregar_Alumno'),
    path('ListAlumno/', listAlumno, name='listAlumno'),
    path('ModificarAlumno/<id>/', modAlumno, name='modAlumno'),
    path('EliminarAlumno/<id>/', eliminarAlumno, name='eliminarAlumno'),

    path('agregar_Profesor/', agregar_Profesor, name="agregar_Profesor"),
    path('ListProf/', listProf, name="listProf"),
    path('ModificarProf/<id>/', modProf, name='modProf'),
    path('EliminarProf/<id>/', eliminarProfesor, name='eliminarProfesor'),

    path('agregarCurso/', agregarCurso, name='agregarCurso'),
    path('ListCurso/', listCurso , name='listCurso'),
    path('ModificarCurso/<id>/', modCursos , name='modCursos'),
    path('EliminarCurso/<id>/', eliminarCurso, name='eliminarCurso'),

    path('AulaComun/', agregarAulaComun, name='agregarAulaComun'),
    path('listAulaComun/', listAulaComun, name='listAulaComun'),
    path('modAulaComun/<id>/', modAula, name = 'modAulaComun'),
    path('EliminarAulaComun/<id>', eliminarAulaComun, name='eliminarAulaComun'),
    path('DetalleAulaComun/<int:pk>/', detalleAulaComun.as_view(), name='DetalleAulaComun'),

    path('agregarControlAsig/', agregarControlAsig, name='agregarControlAsig'),
    path('listControlAsig/', listControlAsig , name='listControlAsig'),
    path('DetalleControlAsig/<int:pk>/', detalleControlAsig.as_view(), name="DetalleControlAsig"),
    path('modControl/<id>/', modControl, name='modControl'),
    path('eliminarControlAsig/<id>/', eliminarControlAsig, name='eliminarControlAsig'),

    path('Anotaciones/', anotaciones, name='anotaciones'),
    path('agregar_Anotacion/', agregar_anotacion, name='agregar_anotacion'),
    path('listaAnotaciones/', lista_anotaciones, name='lista_anotaciones'),
    path('modAnotacion/<id>/', modAnotacion, name='modAnotacion'),
    path('eliminarAsignatura/<id>', eliminarAnotacion, name='eliminarAnotacion'),
    path('DetalleAnotacion/<int:pk>/', detalleAnotacion.as_view(), name='detalleAnotacion'),

    path('agregar_Apoderado/', agregar_Apoderado, name='agregar_Apoderado'),
    path('list_Apoderado/', listar_Apoderados, name ='list_Apoderado'),
    path('ModificarApoderado/<id>/', modApoderados, name ='modApoderado'),
    path('EliminarApoderado/<id>/', eliminarApoderado, name='EliminarApoderado'),

    path('Comunicaciones/',comunicaciones, name='comunicaciones'),
    path('NuevoCorreo/', nuevoCorreo.as_view(), name='nuevoCorreo'),
    path('DetalleCorreo/<int:pk>/', detalleCorreo.as_view(), name='detalleCorreo'),
    path('EditarCorreo/<int:pk>/', updateCorreo.as_view(), name='editarCorreo'),
    path('EliminarCorreo/<int:pk>', eliminarCorreo.as_view(), name='eliminarCorreo'),

    path('Calificaciones/', calificaciones, name='calificaciones'),
    path('agregar_nota/', AgregarNota.as_view(), name='agregarNota'),
    path('notas/', Notas, name='notas'),

    path('', Home, name='home'),
    path('Cursos/', Cursos, name='Cursos'),


    path('Asistencia/', Asistencia, name='asistencia'),
    path('toma_asistencia/', tomaAsistencia, name='tomaAsistencia'),
    path('asistencia_curso/', allAsistencia, name='asistencia_curso'),
    path('modificar_asistecia/<id>/', modAsistecia, name='modificar_asistencia'),
]