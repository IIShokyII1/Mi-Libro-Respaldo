from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,rut,password = None):
        if not email:
            raise ValueError('El Usuario debe tener un correo Electrónico!')
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos,
            rut=rut
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,username,email,nombres,apellidos,rut,password):
        usuario = self.create_user(
            email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            rut=rut,
            password=password
        )
        usuario.usuario_administrador =True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    rol_choices = (
        ('Administrador', 'Administrador'),
        ('Profesor', "Profesor"),
        ('Inspector', "Inspector"),
        ('Apoderado', "Apoderado"),
    )

    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null= True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    rut = models.CharField('rut', max_length=20, unique=True)
    tipo_user = models.CharField('tipo de usuario', max_length=20, choices=rol_choices, default='Administrador')
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects= UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos', 'rut']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador