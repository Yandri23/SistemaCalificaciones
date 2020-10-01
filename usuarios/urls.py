from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from usuarios import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # url(r'^login/$', views.login, name="login"),
    #url(r'^logout/$', views.logout, name="logout"),

    # usuarios

    path('consultarusuarios/', views.consultarusuarios, name="consultarusuarios"),
    path('crearusuario/', views.crearusuario, name="crearusuario"),
    path('modificarusuario/<int:pk>', views.modificarusuario, name="modificarusuario"),
    path('eliminarusuario/<int:pk>', views.eliminarusuario, name="eliminarusuario"),

    # roles

    path('consultar_roles/', views.consultarroles, name="consultarroles"),
    path('crearrol/', views.crearrol, name="crearrol"),
    path('modificarrol/<int:pk>', views.modificarrol, name="modificarrol"),
    path('eliminarrol/<int:pk>', views.eliminarrol, name="eliminarrol"),

    # roles y usuarios relacionados

    path('consultarrolesusuarios/', views.consultarrolesusuarios, name="consultarrolesusuarios"),
    path('crearrolusuario/', views.crearrolusuario, name="crearrolusuario"),
    path('modificarrolusuario/<int:pk>', views.modificarrolusuario, name="modificarrolusuario"),
    path('eliminarrolusuario/<int:pk>', views.eliminarrolusuario, name="eliminarrolusuario"),
]
