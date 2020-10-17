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
    #path('consulta/', views.consulta, name="consulta"),
    path('about-me/', views.about, name="about-me"),
    path('contact/', views.contact, name="contact"),

##CRUD PARA LOS DOCENTES

    path('creardocente/', views.creardocente, name="creardocente"),
    path('modificardocente/<int:pk>', views.modificardocente, name="modificardocente"),
    path('eliminardocente/<int:pk>', views.eliminardocente, name="eliminardocente"),
    path('exportarlistadocentes/', views.exportarlistadocentes, name="exportarlistadocentes"),
    path('docentes/', views.docentes, name="docentes"),
    #path('docentesbydate/', views.docentesbydate, name="docentesbydate"),

##CRUD PARA LOS ALUMNOS

    path('crearestudiante/', views.crearestudiante, name="crearestudiante"),
    path('modificarestudiante/<int:pk>', views.modificarestudiante, name="modificarestudiante"),
    path('eliminarestudiante/<int:pk>', views.eliminarestudiante, name="eliminarestudiante"),
    path('exportarlistaestudiante/', views.exportarlistaestudiante, name="exportarlistaestudiante"),
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
    path('exportarlistaconsulta/', views.exportarlistaconsulta, name="exportarlistaconsulta"),
    path('consulta/', views.consulta, name="consulta"),


##CRUD PARA LOS MATERIA
    path('materiacrear/', views.materiacrear, name="materiacrear"),
    path('materiamodificar/<int:pk>', views.materiamodificar, name="materiamodificar"),
    path('materiaeliminar/<int:pk>', views.materiaeliminar, name="materiaeliminar"),
    path('exportarlistamateria/', views.exportarlistamateria, name="exportarlistamateria"),
    path('materia/', views.materia, name="materia"),

##CRUD DOCENTEMATERIA
    path('docentemateriacrear/', views.docentemateriacrear, name="docentemateriacrear"),
    path('docentemateriamodificar/<int:pk>', views.docentemateriamodificar, name="docentemateriamodificar"),
    path('docentemateriaeliminar/<int:pk>', views.docentemateriaeliminar, name="docentemateriaeliminar"),
    path('docentemateriaexportarlista/', views.docentemateriaexportarlista, name="docentemateriaexportarlista"),
    path('docentemateria/', views.docentemateria, name="docentemateria"),
    path('docentemateriapdf/', views.docentemateriapdf, name="docentemateriapdf"),

##CRUD ESTUDIANTES EN GRADO
    path('estudiantegradocrear/', views.estudiantegradocrear, name="estudiantegradocrear"),
    path('estudiantegradomodificar/<int:pk>', views.estudiantegradomodificar, name="estudiantegradomodificar"),
    path('estudiantegradoeliminar/<int:pk>', views.estudiantegradoeliminar, name="estudiantegradoeliminar"),
    path('exportarlistaestudiantegradopdf/', views.exportarlistaestudiantegradopdf, name="exportarlistaestudiantegradopdf"),
    path('estudiantegradoconsultar/', views.estudiantegradoconsultar, name="estudiantegradoconsultar"),
    path('estudiantegrado/', views.estudiantegrado, name="estudiantegrado"),
    path('estudiantegradopdf/', views.estudiantegradopdf, name="estudiantegradopdf"),

    ##EXTRAS

    path('planificacion/', views.planificacion, name="planificacion"),
    path('usuarios/', include('usuarios.urls'), name="usuarios"),
    path('admin/', admin.site.urls),


]
