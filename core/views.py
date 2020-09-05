from django.contrib.auth.decorators import login_required
from django.forms import models
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Docente
from .forms import DocenteForm


# Create your views here.
html_base = """
    <h1>Mi Menu</h1>
    <ul>
        <li>   <a href="/">Inicio</a>              </li>
        <li>   <a href="/alumnos/">Alumnos</a>   </li>
        <li>   <a href="/docentes/">Docentes</a>   </li>
        <li>   <a href="/calificaciones/">Calificaciones</a>   </li>
        <li>   <a href="/secretaria/">Secretaria</a>   </li>
        <li>   <a href="/about-me/">Acerca de</a>   </li>
        <li>   <a href="/contact/">Contacto</a>     </li>
    </ul>
"""



def home(request):
    html_response = "<h1>la pagina de Portadas</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def contact(request):
    html_response = "<h1>la pagina de Contacto</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def about(request):
    html_response = "<h1>la pagina de Acerca de</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def alumnos(request):
    html_response = "<h1>la pagina de Alumnos</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def docentes(request):
    html_response = "<h1>la pagina de Docentes</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def calificaciones(request):
    html_response = "<h1>la pagina de Calificaciones</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def secretaria(request):
    html_response = "<h1>la pagina de Secretaria</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);


# Template tag
# block content
# extends
# url

def home(request, plantilla="core/home.html"):
    return render(request, plantilla)

def about(request, plantilla="core/about.html"):
    return render(request, plantilla)

def contact(request, plantilla="core/contact.html"):
    return render(request, plantilla)

def alumnos(request, plantilla="core/alumnos.html"):
    return render(request, plantilla)

def docentes(request, plantilla="core/docentes.html"):
    return render(request, plantilla)

def calificaciones(request, plantilla="core/calificaciones.html"):
    return render(request, plantilla)

def secretaria(request, plantilla="core/secretaria.html"):
    return render(request, plantilla)




def index(request):
    return render(request, 'index.html', {'menu': True})


def home(request, plantilla='core/home.html'):
    if request.user.is_authenticated:
        return render(request, plantilla)
    return redirect('login')

#@login_required(None,"", 'loging')
def docentes(request, plantilla="core/docentes.html"):
    docentes = list(Docente.objects.all())
    return render(request, plantilla, {'docentes': docentes})


def cursos(request, plantilla="core/cursos.html"):
    return render(request, plantilla)


def materias(request, plantilla="core/materias.html"):
    return render(request, plantilla)


def planificacion(request, plantilla="core/planificacion.html"):
    return render(request, plantilla)


# take the second element for sort
def take_second(elem):
    return elem[1]




## CREAR DOCENTE CRUD
def creardocente(request, plantilla="core/creardocente.html"):
    if request.method == "POST":
        formDocente = DocenteForm(request.POST)
        if formDocente.is_valid():
            formDocente.save()
            return redirect("docentes")
    else:
        formDocente = DocenteForm()
    return render(request, plantilla, {'formDocente': formDocente})


## MODIFICAR DOCENTE CRUD
def modificardocente(request, pk, plantilla="core/modificardocente.html"):
    if request.method == "POST":
        docente = get_object_or_404(Docente, pk=pk)
        formDocente = DocenteForm(request.POST or None, instance=docente)
        if formDocente.is_valid():
            formDocente.save()
        return redirect("docentes")
    else:
        docente = get_object_or_404(Docente, pk=pk)
        formDocente = DocenteForm(request.POST or None, instance=docente)
    return render(request, plantilla, {'formDocente': formDocente})


## ELIMINAR DOCENTE CRUD
def eliminardocente(request, pk, plantilla="core/eliminardocente.html"):
    if request.method == "POST":
        docente = get_object_or_404(Docente, pk=pk)
        formDocente = DocenteForm(request.POST or None, instance=docente)
        if formDocente.is_valid():
            docente.delete()
        return redirect("docentes")
    else:
        docente = get_object_or_404(Docente, pk=pk)
        formDocente = DocenteForm(request.POST or None, instance=docente)
    return render(request, plantilla, {'formDocente': formDocente})


## CONSULTAR DOCENTE CRUD
def consultardocente(request, plantilla="core/consultardocente.html"):
    return render(request, plantilla)



