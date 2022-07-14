from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from usuario.forms import FormularioLogin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from usuario.models import Usuario
from usuario.forms import FormularioLogin, FormularioUsuario
# Create your views here.

class LoginAdmin(FormView):
    template_name = 'Libro/login/loginCE.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('admin')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginAdmin,self).dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(LoginAdmin,self).form_valid(form)


def logoutAdmin(request):
    logout(request)
    return HttpResponseRedirect('/accounts/loginAdmin/')

class LoginCE(FormView):
    template_name = 'Libro/login/loginCE.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('perfil')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginCE,self).dispatch(request,*args,**kwargs)
    
    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(LoginCE,self).form_valid(form)

def logoutCE(request):
    logout(request)
    return HttpResponseRedirect('/accounts/loginCE/')

class ListadoUsuario(ListView):
    model= Usuario
    template_name = 'usuarios/listar_usuario.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)

class RegistroUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')
