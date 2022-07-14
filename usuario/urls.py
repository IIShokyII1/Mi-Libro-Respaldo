from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import ListadoUsuario, RegistroUsuario

urlpatterns = [
    path('listado_usuarios/', login_required(ListadoUsuario.as_view()), name='listar_usuarios'),
    path('registrar_usuario/', login_required(RegistroUsuario.as_view()), name='registrar_usuario'),
]