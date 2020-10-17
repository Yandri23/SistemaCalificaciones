from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate

from .models import Docente, Estudiante, Grado, Consulta, Materia, Docentemateria, Estudiantegrado
from .forms import DocenteForm, EstudianteForm, GradoForm, ConsultaForm, MateriaForm, DocentemateriaForm, EstudiantegradoForm
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

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

def exportarlistadocentes(request, plantilla="core/docentes.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_docentes.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 6,
                            leftMargin=inch / 6,
                            topMargin=inch / 4,
                            bottomMargin=inch / 6,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    docentes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Docentes", styles['Heading1'])
    docentes.append(header)
    headings = ('Id', 'Nombre', 'Apellido', 'Edad')
    alldocentes = [(d.id, d.nombre, d.apellido, d.edad) for d in Docente.objects.all()]
    print
    alldocentes

    t = Table([headings] + alldocentes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    docentes.append(t)
    doc.build(docentes)
    response.write(buffer.getvalue())
    buffer.close()
    return response



def estudiante(request, plantilla="core/estudiante.html"):
    estudiante = Estudiante.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        estudiante = Estudiante.objects.filter(apellido__contains=search_term)
    return render(request, plantilla, {'estudiante': estudiante})

def exportarlistaestudiante(request, plantilla="core/docentes.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_estudiante.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 6,
                            leftMargin=inch / 6,
                            topMargin=inch / 4,
                            bottomMargin=inch / 6,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    estudiante = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Estudiante", styles['Heading1'])
    estudiante.append(header)
    headings = ('Id', 'Nombre', 'Apellido', 'Edad')
    allestudiante = [(d.id, d.nombre, d.apellido, d.edad) for d in Estudiante.objects.all()]
    print
    allestudiante

    t = Table([headings] + allestudiante)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    estudiante.append(t)
    doc.build(estudiante)
    response.write(buffer.getvalue())
    buffer.close()
    return response



def consulta(request, plantilla="core/consulta.html"):
    estudiante = Estudiante.objects.all()
    grado = Grado.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        estudiante = Estudiante.objects.filter(apellido__contains=search_term)
        grado = Grado.objects.filter(grado__contains=search_term)
    return render(request, plantilla, {'estudiante': estudiante, 'grado': grado})

def exportarlistaconsulta(request, plantilla="core/docentes.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_consulta.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 6,
                            leftMargin=inch / 6,
                            topMargin=inch / 4,
                            bottomMargin=inch / 6,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    consulta = []
    styles = getSampleStyleSheet()
    header = Paragraph("Lista de Consultas", styles['Heading1'])
    consulta.append(header)
    headings = ('Id', 'estudiante', 'grado')
    allconsulta = [(d.id, d.estudiante, d.grado) for d in Consulta.objects.all()]
    print
    allconsulta

    t = Table([headings] + allconsulta)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consulta.append(t)
    doc.build(consulta)
    response.write(buffer.getvalue())
    buffer.close()
    return response




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

def exportarlistamateria(request, plantilla="core/docentes.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_materia.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 6,
                            leftMargin=inch / 6,
                            topMargin=inch / 4,
                            bottomMargin=inch / 6,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    materia = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de materia", styles['Heading1'])
    materia.append(header)
    headings = ('Id', 'Materia')
    allmateria = [(d.id, d.materia) for d in Materia.objects.all()]
    print
    allmateria

    t = Table([headings] + allmateria)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    materia.append(t)
    doc.build(materia)
    response.write(buffer.getvalue())
    buffer.close()
    return response




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
            grado.delete()
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
           formConsulta.delete()
       return redirect("consulta")
    else:
        consulta = get_object_or_404(Consulta, pk=pk)
        formConsulta = ConsultaForm(request.POST or None, instance=consulta)
    return render(request, plantilla, {'formConsulta': formConsulta})


# CONSULTAR CONSULTA CRUD
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
            materia.delete()
        return redirect("materia")
    else:
        materia = get_object_or_404(Materia, pk=pk)
        formMateria = MateriaForm(request.POST or None, instance=materia)
    return render(request, plantilla, {'formMateria': formMateria})

## CONSULTAR MATERIA CRUD
def materiaconsultar(request, plantilla="core/materiaconsultar.html"):
    return render(request, plantilla)

## DOCENTEMATERIA CRUD

def docentemateria(request, plantilla="core/docentemateria.html"):
    docentemateria = Docentemateria.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        docentemateria = Docentemateria.objects.filter(docentemateria__contains=search_term)
    return render(request, plantilla, {'docentemateria': docentemateria})


def docentemateriapdf(request, plantilla="core/docentemateriapdf.html"):
    docentemateria = list(Docentemateria.objects.all())
    return render(request, plantilla, {'docentemateria': docentemateria})

#    docentemateria = Docentemateria.objects.all()
#    if 'search' in request.GET:
#        search_term = request.GET['search']
#        docentemateria = Docentemateria.objects.filter(docente__contains=search_term)
#    return render(request, plantilla, {'docentemateria': docentemateria})


def docentemateriacrear(request, plantilla="core/docentemateriacrear.html"):
    if request.method == "POST":
        formDocentemateria = DocentemateriaForm(request.POST)
        if formDocentemateria.is_valid():
            formDocentemateria.save()
            return redirect("docentemateria")
    else:
        formDocentemateria = DocentemateriaForm()
    return render(request, plantilla, {'formDocentemateria': formDocentemateria})

def docentemateriamodificar(request, pk, plantilla="core/docentemateriamodificar.html"):
    if request.method == "POST":
        docentemateria = get_object_or_404(Docentemateria, pk=pk)
        formDocentemateria = DocentemateriaForm(request.POST or None, instance=docentemateria)
        if formDocentemateria.is_valid():
            formDocentemateria.save()
        return redirect("docentemateria")
    else:
        docentemateria = get_object_or_404(Docentemateria, pk=pk)
        formDocentemateria = DocentemateriaForm(request.POST or None, instance=docentemateria)
    return render(request, plantilla, {'formDocentemateria': formDocentemateria})

def docentemateriaeliminar(request, pk, plantilla="core/docentemateriaeliminar.html"):
    if request.method == "POST":
        docentemateria = get_object_or_404(Docentemateria, pk=pk)
        formDocentemateria = DocentemateriaForm(request.POST or None, instance=docentemateria)
        if formDocentemateria.is_valid():
            docentemateria.delete()
        return redirect("docentemateria")
    else:
        docentemateria = get_object_or_404(Docentemateria, pk=pk)
        formDocentemateria = DocentemateriaForm(request.POST or None, instance=docentemateria)
    return render(request, plantilla, {'formDocentemateria': formDocentemateria})


def docentemateriaexportarlista(request, plantilla="core/docentes.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_Docentemateria.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 6,
                            leftMargin=inch / 6,
                            topMargin=inch / 4,
                            bottomMargin=inch / 6,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    docentemateria = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Docente materia", styles['Heading1'])
    docentemateria.append(header)
    headings = ('Id', 'Docente', 'Materia')
    alldocentemateria = [(d.id,d.docente, d.materia) for d in Docentemateria.objects.all()]
    print
    alldocentemateria

    t = Table([headings] + alldocentemateria)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    docentemateria.append(t)
    doc.build(docentemateria)
    response.write(buffer.getvalue())
    buffer.close()
    return response

############################
## CREAR ESTUDIANTE GRADO ##
############################
def estudiantegrado(request, plantilla="core/estudiantegrado.html"):
    estudiantegrado = Estudiantegrado.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        estudiantegrado = Estudiantegrado.objects.filter(estudiantegrado__contains=search_term)
    return render(request, plantilla, {'estudiantegrado': estudiantegrado})

def estudiantegradopdf(request, plantilla="core/estudiantegradopdf.html"):
    estudiantegrado = list(Estudiantegrado.objects.all())
    return render(request, plantilla, {'estudiantegrado': estudiantegrado})

def exportarlistaestudiantegradopdf(request, plantilla="core/docentes.html"):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="listade_de_Estudiantes_en_Grado.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 6,
                            leftMargin=inch / 6,
                            topMargin=inch / 4,
                            bottomMargin=inch / 6,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    estudiantegradopdf = []
    styles = getSampleStyleSheet()
    header = Paragraph("Lista de Estudiantes en Grado", styles['Heading1'])
    estudiantegradopdf.append(header)
    headings = ('Id', 'estudiante', 'grado')
    allestudiantegradopdf = [(d.id, d.estudiante, d.grado) for d in Estudiantegrado.objects.all()]
    print
    allestudiantegradopdf

    t = Table([headings] + allestudiantegradopdf)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    estudiantegradopdf.append(t)
    doc.build(estudiantegradopdf)
    response.write(buffer.getvalue())
    buffer.close()
    return response

## CREAR ESTUDIANTE GRADO
def estudiantegradocrear(request, plantilla="core/estudiantegradocrear.html"):
    if request.method == "POST":
        formEstudiantegrado = EstudiantegradoForm(request.POST)
        if formEstudiantegrado.is_valid():
            formEstudiantegrado.save()
            return redirect("estudiantegrado")
    else:
        formEstudiantegrado = EstudiantegradoForm()
    return render(request, plantilla, {'formEstudiantegrado': formEstudiantegrado})


## MODIFICAR ESTUDIANTE GRADO
def estudiantegradomodificar(request, pk, plantilla="core/estudiantegradomodificar.html"):
    if request.method == "POST":
        estudiantegrado = get_object_or_404(Estudiantegrado, pk=pk)
        formEstudiantegrado = EstudiantegradoForm(request.POST or None, instance=estudiantegrado)
        if formEstudiantegrado.is_valid():
            formEstudiantegrado.save()
        return redirect("estudiantegrado")
    else:
        estudiantegrado = get_object_or_404(Estudiantegrado, pk=pk)
        formEstudiantegrado = EstudiantegradoForm(request.POST or None, instance=estudiantegrado)

    return render(request, plantilla, {'formEstudiantegrado': formEstudiantegrado})


## ELIMINAR ESTUDIANTE GRADO
def estudiantegradoeliminar(request, pk, plantilla="core/estudiantegradoeliminar.html"):
    if request.method == "POST":
        estudiantegrado = get_object_or_404(Estudiantegrado, pk=pk)
        formEstudiantegrado = EstudiantegradoForm(request.POST or None, instance=estudiantegrado)
        if formEstudiantegrado.is_valid():
            estudiantegrado.delete()
        return redirect("estudiantegrado")
    else:
        estudiantegrado = get_object_or_404(Estudiantegrado, pk=pk)
        formEstudiantegrado = EstudiantegradoForm(request.POST or None, instance=estudiantegrado)
    return render(request, plantilla, {'formEstudiantegrado': formEstudiantegrado})


## CONSULTAR ESTUDIANTE GRADO
def estudiantegradoconsultar(request, plantilla="core/estudiantegrado.html"):
    return render(request, plantilla)
