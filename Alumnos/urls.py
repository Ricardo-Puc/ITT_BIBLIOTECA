from django.contrib import admin
from django.urls import path
from .views import home, loginPage, registro, logoutUser, actualizar, perfil, libros, revistas, residencia, estadisticas, desarrollador, CreateResidencia

urlpatterns = [
    path('', loginPage, name="loginPage"),
    path('logout/',logoutUser, name = 'logout'),
    path('home/', home, name="home"),
    path('perfil/', perfil, name="perfil"),
    path('libros/', libros, name="libros"),
    path('revistas/', revistas, name="revistas"),
    path('residencia/', residencia, name="residencia"),
    path('estadisticas/', estadisticas, name="estadisticas"),
    path('registro/', registro, name="registro"),
    path('actualizar/', actualizar, name="actualizar"),
    path('desarrollador/', desarrollador, name="desarrollador"),
    path('subir/', CreateResidencia.as_view(), name="subir"),
] 