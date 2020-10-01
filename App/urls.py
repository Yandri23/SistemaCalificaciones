"""App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('estudiante/', views.estudiante, name="estudiante"),
    path('docentes/', views.docentes, name="Docentes"),
    path('calificaciones/', views.calificaciones, name="Calificaciones"),
    path('secretaria/', views.secretaria, name="secretaria"),
    path('consulta/', views.consulta, name="consulta"),
    path('about-me/', views.about, name="about-me"),
    path('contact/', views.contact, name="contact"),

##CRUD PARA LOS DOCENTES

    path('creardocente/', views.creardocente, name="creardocente"),
    path('modificardocente/<int:pk>', views.modificardocente, name="modificardocente"),
    path('eliminardocente/<int:pk>', views.eliminardocente, name="eliminardocente"),
    path('docentes/', views.docentes, name="docentes"),

##CRUD PARA LOS ALUMNOS

    path('crearestudiante/', views.crearestudiante, name="crearestudiante"),
    path('modificarestudiante/<int:pk>', views.modificarestudiante, name="modificarestudiante"),
    path('eliminarestudiante/<int:pk>', views.eliminarestudiante, name="eliminarestudiante"),
    path('estudiante/', views.estudiante, name="estudiante"),

##CRUD PARA LOS GRADOS

    path('creargrado/', views.creargrado, name="creargrado"),
    path('modificargrado/<int:pk>', views.modificargrado, name="modificargrado"),
    path('eliminargrado/<int:pk>', views.eliminargrado, name="eliminargrado"),
    path('grado/', views.grado, name="grado"),

##CRUD PARA LOS CONSULTA
    path('crearconsulta/', views.crearconsulta, name="crearconsulta"),
    path('modificarconsulta/<int:pk>', views.modificarconsulta, name="modificarconsulta"),
    path('eliminarconsulta/<int:pk>', views.eliminarconsulta, name="eliminarconsulta"),
    path('consulta/', views.consulta, name="consulta"),




    path('materias/', views.materias, name="materias"),
    path('planificacion/', views.planificacion, name="planificacion"),
    path('usuarios/', include('usuarios.urls'), name="usuarios"),
    path('admin/', admin.site.urls),


]
