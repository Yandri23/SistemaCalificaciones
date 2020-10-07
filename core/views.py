from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Docente, Estudiante, Grado, Consulta, Materia
from .forms import DocenteForm, EstudianteForm, GradoForm, ConsultaForm, MateriaForm

# Create your views here.
html_base = """
    <h1>Mi Menu</h1>
    <ul>
        <li>   <a href="/">Inicio</a>              </li>
        <li>   <a href="/estudiante/">Estudiante</a>   </li>
        <li>   <a href="/curso/">Curso</a>   </li>
        <li>   <a href="/docentes/">Docentes</a>   </li>
        <li>   <a href="/calificaciones/">Calificaciones</a>   </li>
        <li>   <a href="/secretaria/">Secretaria</a>   </li>
        <li>   <a href="/consulta/">Consulta</a>   </li>
        <li>   <a href="/about-me/">Acerca de</a>   </li>
        <li>   <a href="/contact/">Contacto</a>     </li>
    </ul>
"""


def home(request, plantilla="core/home.html"):
    return render(request, plantilla)



def about(request, plantilla="core/about.html"):
    return render(request, plantilla)


def contact(request, plantilla="core/contact.html"):
    return render(request, plantilla)



def calificaciones(request, plantilla="core/calificaciones.html"):
    return render(request, plantilla)


def secretaria(request, plantilla="core/secretaria.html"):
    return render(request, plantilla)


def home(request, plantilla='core/home.html'):
    if request.user.is_authenticated:
        return render(request, plantilla)
    return redirect('login')



@login_required(None, "", 'login')
def docentes(request, plantilla="core/docentes.html"):
    docentes = Docente.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        docentes = Docente.objects.filter(apellido__contains=search_term)
    return render(request, plantilla, {'docentes': docentes})


def estudiante(request, plantilla="core/estudiante.html"):
    estudiante = Estudiante.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        estudiante = Estudiante.objects.filter(apellido__contains=search_term)
    return render(request, plantilla, {'estudiante': estudiante})


def consulta(request, plantilla="core/consulta.html"):
    estudiante = Estudiante.objects.all()
    grado = Grado.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        estudiante = Estudiante.objects.filter(apellido__contains=search_term)
        grado = Grado.objects.filter(grado__contains=search_term)
    return render(request, plantilla, {'estudiante': estudiante, 'grado': grado})


def grado(request, plantilla="core/grado.html"):
    grado = Grado.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        grado = Grado.objects.filter(grado__contains=search_term)
    return render(request, plantilla, {'grado': grado})


def materia(request, plantilla="core/materia.html"):
    materia = Materia.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        materia = Materia.objects.filter(materia__contains=search_term)
    return render(request, plantilla, {'materia': materia})

def planificacion(request, plantilla="core/planificacion.html"):
    return render(request, plantilla)


# take the second element for sort
def take_second(elem):
    return elem[1]


#############################################
############    CRUB DOCENTES     ###########
#############################################

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


################## ALUMNO CRUD  ##################

## CREAR ALUMNO CRUD

def crearestudiante(request, plantilla="core/crearestudiante.html"):
    if request.method == "POST":
        formEstudiante = EstudianteForm(request.POST)
        if formEstudiante.is_valid():
            formEstudiante.save()
            return redirect("estudiante")
    else:
        formEstudiante = EstudianteForm()
    return render(request, plantilla, {'formEstudiante': formEstudiante})


## MODIFICAR ALUMNO CRUD
def modificarestudiante(request, pk, plantilla="core/modificarestudiante.html"):
    if request.method == "POST":
        estudiante = get_object_or_404(Estudiante, pk=pk)
        formEstudiante = EstudianteForm(request.POST or None, instance=estudiante)
        if formEstudiante.is_valid():
            formEstudiante.save()
        return redirect("estudiante")
    else:
        estudiante = get_object_or_404(Estudiante, pk=pk)
        formEstudiante = EstudianteForm(request.POST or None, instance=estudiante)
    return render(request, plantilla, {'formEstudiante': formEstudiante})


## ELIMINAR ALUMNO CRUD
def eliminarestudiante(request, pk, plantilla="core/eliminarestudiante.html"):
    if request.method == "POST":
        estudiante = get_object_or_404(Estudiante, pk=pk)
        formEstudiante = EstudianteForm(request.POST or None, instance=estudiante)
        if formEstudiante.is_valid():
            estudiante.delete()
        return redirect("estudiante")
    else:
        estudiante = get_object_or_404(Estudiante, pk=pk)
        formEstudiante = EstudianteForm(request.POST or None, instance=estudiante)
    return render(request, plantilla, {'formEstudiante': formEstudiante})


## CONSULTAR ALUMNO CRUD
def consultarestudiante(request, plantilla="core/consultarestudiante.html"):
    return render(request, plantilla)


################## CURSO CRUD  ##################

## CREAR CURSO CRUD

def creargrado(request, plantilla="core/creargrado.html"):
    if request.method == "POST":
        formGrado = GradoForm(request.POST)
        if formGrado.is_valid():
            formGrado.save()
            return redirect("grado")
    else:
        formGrado = GradoForm()
    return render(request, plantilla, {'formGrado': formGrado})


## MODIFICAR CURSO CRUD
def modificargrado(request, pk, plantilla="core/modificargrado.html"):
    if request.method == "POST":
        grado = get_object_or_404(Grado, pk=pk)
        formGrado = GradoForm(request.POST or None, instance=grado)
        if formGrado.is_valid():
            formGrado.save()
        return redirect("grado")
    else:
        grado = get_object_or_404(Grado, pk=pk)
        formGrado = GradoForm(request.POST or None, instance=grado)
    return render(request, plantilla, {'formGrado': formGrado})


## ELIMINAR CURSO CRUD
def eliminargrado(request, pk, plantilla="core/eliminargrado.html"):
    if request.method == "POST":
        grado = get_object_or_404(Grado, pk=pk)
        formGrado = GradoForm(request.POST or None, instance=grado)
        if formGrado.is_valid():
            formGrado.save()
        return redirect("grado")
    else:
        grado = get_object_or_404(Grado, pk=pk)
        formGrado = GradoForm(request.POST or None, instance=grado)
    return render(request, plantilla, {'formGrado': formGrado})


## CONSULTAR CURSO CRUD
def consultargrado(request, plantilla="core/consultargrado.html"):
    return render(request, plantilla)


################## CONSULTA CRUD  ##################

## CREAR CONSULTA CRUD

def crearconsulta(request, plantilla="core/crearconsulta.html"):
    if request.method == "POST":
        formConsulta = ConsultaForm(request.POST)
        if formConsulta.is_valid():
            formConsulta.save()
            return redirect("consulta")
    else:
        formConsulta = ConsultaForm()
    return render(request, plantilla, {'formConsulta': formConsulta})



## MODIFICAR CONSULTA CRUD
def modificarconsulta(request, pk, plantilla="core/modificarconsulta.html"):
    if request.method == "POST":
        consulta = get_object_or_404(Consulta, pk=pk)
        formConsulta = ConsultaForm(request.POST or None, instance=consulta)
        if formConsulta.is_valid():
            formConsulta.save()
        return redirect("consulta")
    else:
        consulta = get_object_or_404(Consulta, pk=pk)
        formConsulta = ConsultaForm(request.POST or None, instance=consulta)
    return render(request, plantilla, {'formConsulta': formConsulta})


## ELIMINAR CONSULTA CRUD
def eliminarconsulta(request, pk, plantilla="core/eliminarconsulta.html"):
    if request.method == "POST":
        consulta = get_object_or_404(Consulta, pk=pk)
        formConsulta = ConsultaForm(request.POST or None, instance=consulta)
        if formConsulta.is_valid():
            formConsulta.save()
        return redirect("consulta")
    else:
        consulta = get_object_or_404(Consulta, pk=pk)
        formConsulta = ConsultaForm(request.POST or None, instance=consulta)
    return render(request, plantilla, {'formConsulta': formConsulta})


## CONSULTAR CONSULTA CRUD
def consultarconsulta(request, plantilla="core/consultarconsulta.html"):
    return render(request, plantilla)


################## MATERIAS CRUD  ##################

## CREAR MATERIA CRUD

def materiacrear(request, plantilla="core/materiacrear.html"):
    if request.method == "POST":
        formMateria = MateriaForm(request.POST)
        if formMateria.is_valid():
            formMateria.save()
            return redirect("materia")
    else:
        formMateria = MateriaForm()
    return render(request, plantilla, {'formMateria': formMateria})


## MODIFICAR MATERIA CRUD
def materiamodificar(request, pk, plantilla="core/materiamodificar.html"):
    if request.method == "POST":
        materia = get_object_or_404(Materia, pk=pk)
        formMateria = MateriaForm(request.POST or None, instance=materia)
        if formMateria.is_valid():
            formMateria.save()
        return redirect("materia")
    else:
        materia = get_object_or_404(Materia, pk=pk)
        formMateria = MateriaForm(request.POST or None, instance=materia)
    return render(request, plantilla, {'formMateria': formMateria})

## ELIMINAR MATERIA CRUD
def materiaeliminar(request, pk, plantilla="core/materiaeliminar.html"):
    if request.method == "POST":
        materia = get_object_or_404(Materia, pk=pk)
        formMateria = MateriaForm(request.POST or None, instance=materia)
        if formMateria.is_valid():
            formMateria.save()
        return redirect("materia")
    else:
        materia = get_object_or_404(Materia, pk=pk)
        formMateria = MateriaForm(request.POST or None, instance=materia)
    return render(request, plantilla, {'formMateria': formMateria})

## CONSULTAR MATERIA CRUD
def materiaconsultar(request, plantilla="core/materiaconsultar.html"):
    return render(request, plantilla)