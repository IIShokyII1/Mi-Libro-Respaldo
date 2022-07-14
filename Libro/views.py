import re
from django import views
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView, CreateView, ListView, TemplateView
from .models import (Alumno,Profesor, Curso, Anotacion, AulaComun, ControlAsignatura, Apoderado, Comunicacion, Calificaciones, asistencia)
from django.http import Http404
from .forms import  (AlumnosForm, CalificacionForm, ProfesorForm, CursoForm, AulaForm, AnotacionForm, ControlForm, ApoderadoForm , ComunicacionForm, 
                     AsistenciaForm )
from django.core.paginator import Paginator
from .filters import OrderFilter, AsistenciaFilter, ControlFilter, AulaFilter, AnotacionFilter
# Create your views here.



def admin(request):
    return render(request, 'Libro/Admins/Admin.html')

def perfil(request):
    return render(request, 'Libro/LibroClases/perfil.html')

def agregar_Alumno(request):

    data = {
        'form': AlumnosForm
    }
    
    if request.method == 'POST':
        formulario = AlumnosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data['form'] = formulario

    return render(request, 'Libro/Admins/Alumnos/regisAlumno.html', data)

def listAlumno(request):
    alumnos = Alumno.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(alumnos, 5)
        alumnos = paginator.page(page)
    except: 
        raise Http404
    
    data = {
        'entity': alumnos,
        'paginator': paginator
    }
    return render(request, "Libro/Admins/Alumnos/listAlumno.html", data)

def modAlumno(request, id):
    alumno = get_object_or_404(Alumno, id = id)

    data = {
        'form': AlumnosForm(instance=alumno)
    }

    if request.method == 'POST':
        formulario = AlumnosForm(data=request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listAlumno")
        data['form'] = formulario
    return render(request, 'Libro/Admins/Alumnos/modAlumno.html', data)

def eliminarAlumno(request, id):
    alumno = get_object_or_404(Alumno, id = id)
    alumno.delete()
    return redirect(to='listAlumno')

def agregar_Profesor(request):

    data = {
        'form': ProfesorForm()
    }
    if request.method == 'POST':
        formulario = ProfesorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "Profesor Guardado Correctamente"
        else:
            data["form"] = formulario

    return render(request, 'Libro/Admins/Docentes/regisProf.html', data)

def listProf(request):
    profesores = Profesor.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(profesores, 1)
        profesores = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': profesores,
        'paginator': paginator
    }
    return render(request, "Libro/Admins/Docentes/listProf.html", data)

def modProf(request, id):
    profesor = get_object_or_404(Profesor, id = id)

    data = {
        'form': ProfesorForm(instance=profesor)
    }

    if request.method == 'POST':
        formulario = ProfesorForm(data=request.POST, instance=profesor)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listProf")
        data["form"] = formulario     

    return render(request, 'Libro/Admins/Docentes/modProf.html', data)

def eliminarProfesor(request, id):
    profesor = get_object_or_404(Profesor, id = id)
    profesor.delete()
    return redirect(to="listProf")

def agregarCurso(request):
    data = {
        'form': CursoForm()
    }

    if request.method == 'POST':
        formulario = CursoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Cursos guardado"
        else:
            data['form'] = formulario
    return render(request, 'Libro/Admins/Cursos/regisCurso.html', data)

def listCurso(request):
    cursos = Curso.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(cursos, 2)
        cursos = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': cursos,
        'paginator': paginator

    }
    return render(request, "Libro/Admins/Cursos/listCurso.html", data)

def modCursos(request, id):
    cursos = get_object_or_404(Curso, id = id)

    data = {
        'form': CursoForm(instance=cursos)
    }

    if request.method == 'POST':
        formulario = CursoForm(data=request.POST, instance= cursos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listCurso")
        data['form'] = formulario

    return render(request, "Libro/Admins/Cursos/modCurso.html", data)

def eliminarCurso(request, id):
    cursos = get_object_or_404(Curso, id = id)
    cursos.delete()
    return redirect(to='listCurso')

def agregarControlAsig(request):
    data = {
        'form': ControlForm()
    }

    if request.method =='POST':
        formulario = ControlForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Control guardado"
        else:
            data['form'] = formulario
    return render(request, 'Libro/LibroClases/ControlAsig/ControlAsig.html', data)

def listControlAsig(request):
    controlasignaturas = ControlAsignatura.objects.all()
    try:
       orders = controlasignaturas.order_by()
       order_count = orders.count()

       filtroControl = ControlFilter(request.GET, queryset = orders)
       orders = filtroControl.qs

    except:
        raise Http404

    data = {
        'controlasignaturas': controlasignaturas,
        'orders': orders,
        'order_count': order_count,
        'filtroControl': filtroControl
    }
    return render(request, "Libro/LibroClases/ControlAsig/listControl.html", data)

class detalleControlAsig(View):
    def get(self, request, pk, *args, **kwargs):
        control = get_object_or_404(ControlAsignatura, pk=pk)
        context={
            'control':control
        }
        return render(request, 'Libro/LibroClases/ControlAsig/detalleControl.html', context)

def modControl(request, id):
    controlasignaturas = get_object_or_404(ControlAsignatura, id = id)

    data = {
        'form': ControlForm(instance=controlasignaturas)
    }

    if request.method == 'POST':
        formulario = ControlForm(data=request.POST, instance= controlasignaturas)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listControlAsig")
        data['form'] = formulario

    return render(request, "Libro/LibroClases/ControlAsig/modControl.html", data)

def eliminarControlAsig(request, id):
    controlasignaturas = get_object_or_404(ControlAsignatura, id = id)
    controlasignaturas.delete()
    return redirect(to='listControlAsig')


def agregarAulaComun(request):
    data = {
      'form': AulaForm()
    }

    if request.method == 'POST':
        formulario = AulaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro guardado"
        else:
            data['form'] = formulario
    return render(request, 'Libro/LibroClases/AulaComun/AulaComun.html', data)

def listAulaComun(request):
    aulacomun = AulaComun.objects.all()
    
    try:
        orders = aulacomun.order_by()
        order_count = orders.count()

        filtroAulaComun = AulaFilter(request.GET, queryset=orders)
        orders = filtroAulaComun.qs

    except:
        raise Http404
    data = {
        'aulacomun': aulacomun,
        'orders': orders,
        'order_count': order_count,
        'filtroAulaComun': filtroAulaComun,
    }
    return render(request, "Libro/LibroClases/AulaComun/listAulaComun.html", data)

class detalleAulaComun(View):
    def get(self, request, pk, *args, **kwargs):
        aulacomun=get_object_or_404(AulaComun, pk=pk)
        context={
            'aulacomun': aulacomun
        }
        return render(request, 'Libro/LibroClases/AulaComun/detalleAulaComun.html', context)

def modAula(request, id):
    aulacomun = get_object_or_404(AulaComun, id = id)

    data = {
        'form': AulaForm(instance = aulacomun)
    }
    if request.method == 'POST':
        formulario = AulaForm(data=request.POST, instance= aulacomun)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listAulaComun")
        data['form'] = formulario
    return render(request, "Libro/LibroClases/AulaComun/modAulaComun.html", data)

def eliminarAulaComun(request, id):
    aulacomun = get_object_or_404(AulaComun, id = id)
    aulacomun.delete()
    return redirect(to='listAulaComun')

def anotaciones(request):
    alumnos = Alumno.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(alumnos, 4)
        alumnos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': alumnos,
        'paginator': paginator
    }
    return render(request, "Libro/LibroClases/Anotaciones/Anotacion.html", data)

class detalleAnotacion(View):
    def get(self, request, pk,*args, **kwargs):
        anotacion=get_object_or_404(Anotacion, pk=pk)
        context={
            'anotacion': anotacion
        }

        return render(request, 'Libro/LibroClases/Anotaciones/detalleAnotacion.html', context)

def agregar_anotacion(request):
    data = {
        'form': AnotacionForm()
    }

    if request.method == 'POST':
        formulario = AnotacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lista_anotaciones")
        else:
            data['form'] = formulario
    return render(request, 'Libro/LibroClases/Anotaciones/regisAnotacion.html', data)

def lista_anotaciones(request):
    
    anotacion = Anotacion.objects.all()
    
    
    try:
        orders = anotacion.order_by()
        order_count= orders.count()

        filtroAnotacion = AnotacionFilter(request.GET, queryset = orders)
        orders = filtroAnotacion.qs
    except:
        raise Http404
    
    data = {
        'anotacion': anotacion,
        'orders': orders,
        'order_count': order_count,
        'filtroAnotacion': filtroAnotacion
    }
    return render(request, "Libro/LibroClases/Anotaciones/listAnotacion.html", data)

def modAnotacion(request, id):
    anotacion = get_object_or_404(Anotacion, id = id)

    data = {
        'form': AnotacionForm(instance=anotacion)
    }

    if request.method == 'POST':
        formulario = AnotacionForm(data=request.POST, instance= anotacion)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lista_anotaciones")
        data['form'] = formulario
    return render(request, "Libro/LibroClases/Anotaciones/modAnotacion.html", data)

def eliminarAnotacion(request, id):
    anotacion = get_object_or_404(Anotacion, id = id)
    anotacion.delete()
    return redirect(to='lista_anotaciones')

def agregar_Apoderado(request):
    data = {
        'form': ApoderadoForm()
    }
    if request.method == 'POST':
        formulario = ApoderadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["Mensaje"] = "Apoderado creado "
        else:
            data['form'] = formulario
    return render(request, 'Libro/Admins/Apoderados/regisApode.html', data)

def listar_Apoderados(request):
    apoderados = Apoderado.objects.all()

    page = request.GET.get('page',1)
    try:
        paginator = Paginator(apoderados, 10)
        apoderados = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': apoderados,
        'paginator': paginator
    }
    return render(request, "Libro/Admins/Apoderados/listApoderado.html", data)

def modApoderados(request, id):
    apoderados = get_object_or_404(Apoderado, id = id)

    data = {
        'form': ApoderadoForm(instance=apoderados)
    } 

    if request.method == 'POST':
        formulario = ApoderadoForm(data=request.POST, instance= apoderados)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='list_Apoderado')  
        data['form'] = formulario
    return render(request, "Libro/Admins/Apoderados/modApoderado.html", data)

def eliminarApoderado(request, id):
    apoderados = get_object_or_404(Apoderado, id=id)
    apoderados.delete()
    return redirect(to='list_Apoderado') 

def comunicaciones(request):
    comunicacion = Comunicacion.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(comunicacion, 2)
        comunicacion = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': comunicacion,
        'paginator': paginator
    }
    return render(request, 'Libro/LibroClases/Comunicaciones/comunicacion.html', data)

class nuevoCorreo(View):
    def get(self, request, *args, **kwargs):
        form= ComunicacionForm()
        context={
            'form': form
        }
        return render(request, 'Libro/LibroClases/Comunicaciones/nuevoCorreo.html', context)
    
    def post(self, request, *args, **kwargs):
        

        if request.method=="POST":
            form= ComunicacionForm(request.POST or None)

            if form.is_valid():
                instance=form.save()
                newsletter=Comunicacion.objects.get(id=instance.id)

                if newsletter.status=="Publicado":
                    subject = newsletter.subject
                    body = newsletter.body
                    from_email = settings.EMAIL_HOST_USER
                    for correo in newsletter.correo.all():
                        send_mail(subject=subject, from_email=from_email, recipient_list=[correo], message=body, fail_silently=True)
                return redirect('comunicaciones')
        context={
            'form': form
        }
        return render(request, 'Libro/LibroClases/Comunicaciones/nuevoCorreo.html', context)

class detalleCorreo(View):
    def get(self, request, pk,*args, **kwargs):
        newsletter=get_object_or_404(Comunicacion, pk=pk)
        context={
            'newsletter':newsletter
        } 
        return render(request, 'Libro/LibroClases/Comunicaciones/detalleCorreo.html', context)

class updateCorreo(UpdateView):
    model=Comunicacion
    form_class=ComunicacionForm
    template_name='Libro/LibroClases/Comunicaciones/editarCorreo.html'
    success_url= '/DetalleCorreo/9/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context
    
    def post(self, request, pk, *args, **kwargs):
        newsletter=get_object_or_404(Comunicacion, pk=pk)

        if request.method=="POST":
            form= ComunicacionForm(request.POST or None)

            if form.is_valid():
                instance=form.save()
                newsletter=Comunicacion.objects.get(id=instance.id)

                if newsletter.status=="Publicado":
                    subject = newsletter.subject
                    body = newsletter.body
                    from_email = settings.EMAIL_HOST_USER
                    for correo in newsletter.correo.all():
                        send_mail(subject=subject, from_email=from_email, recipient_list=[correo], message=body, fail_silently=True)
                return redirect(to='detalleCorreo', pk=newsletter.id)
            return redirect(to='detalleCorreo', pk=newsletter.id)
        else:
            form=ComunicacionForm(instance=newsletter)
        context={
            'form': form
        }
        return render(request, 'Libro/LibroClases/Comunicaciones/editarCorreo.html', context)

class eliminarCorreo(DeleteView):
    model=Comunicacion
    template_name='Libro/LibroClases/Comunicaciones/eliminarCorreo.html'
    success_url='/Comunicaciones/'

def calificaciones(request):
    alumnos = Alumno.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(alumnos, 10)
        alumnos = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': alumnos,
        'paginator': paginator
    }
    return render(request, 'Libro/LibroClases/Calificaciones/Alumnos.html', data)

class AgregarNota(CreateView):
    model= Calificaciones
    form_class = CalificacionForm
    template_name = 'Libro/LibroClases/Calificaciones/agregarNota.html'
    success_url = reverse_lazy('calificaciones')

def Notas(request):
    nota = Calificaciones.objects.all()
    
    try:
        orders = nota.order_by()
        order_count = orders.count()

        myFilter = OrderFilter(request.GET, queryset=orders)
        orders = myFilter.qs

    except:
        raise Http404
    data = {
        'nota': nota,
        'orders':orders,
        'order_count': order_count,
        'myFilter': myFilter,
    }
    return render(request, 'Libro/LibroClases/Calificaciones/listadoNotas.html', data)

def Home(request):
    return render(request, 'Libro/HomeMilibro/home.html')

def Cursos(request):
    return render(request, 'Libro/HomeMilibro/curso.html')  

def Asistencia(request):
    alumnos = Alumno.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(alumnos, 7)
        alumnos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': alumnos,
        'paginator': paginator
    }

    return render(request, 'Libro/LibroClases/Asistencia/asistencia.html', data)

def tomaAsistencia(request):
    data = {
        'form': AsistenciaForm()
    }
    if request.method == 'POST':
        formulario = AsistenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('asistencia')
        else:
            data['form'] = formulario
    return render(request, 'Libro/LibroClases/Asistencia/tomaAsistencia.html', data)

def allAsistencia(request):
    asis = asistencia.objects.all()
    
    try:
       orders = asis.order_by()
       order_count = orders.count()

       miFiltro = AsistenciaFilter(request.GET, queryset=orders)
       orders = miFiltro.qs
    except:
        raise Http404
    data = {
        'asis': asis,
        'orders': orders,
        'orders_count': order_count,
        'miFiltro': miFiltro,
    }

    return render(request, 'Libro/LibroClases/Asistencia/allAsistencia.html', data)

def modAsistecia(request, id):
    asis = get_object_or_404(asistencia, id = id)

    data = {
        'form': AsistenciaForm(instance=asis)
    }

    if request.method == 'POST':
        formulario = AsistenciaForm(data=request.POST, instance=asis)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='asistencia_curso')
        data['form'] = formulario
    return render(request, 'Libro/LibroClases/Asistencia/modAsistecia.html', data)