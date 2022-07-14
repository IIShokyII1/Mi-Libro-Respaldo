"""MiLibro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from usuario.views import LoginAdmin, LoginCE, logoutAdmin, logoutCE
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('usuario.urls', 'usuarios'))),
    path('',include('Libro.urls')),
    path('accounts/loginAdmin/', LoginAdmin.as_view(), name='loginAdmin'),
    path('logoutAdmin/', login_required(logoutAdmin) , name='logoutAdmin'),

    path('accounts/loginCE/', LoginCE.as_view(), name='loginCE'),
    path('logoutCE/', login_required(logoutCE), name='logoutCE'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
