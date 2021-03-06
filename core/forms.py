from django import forms
from .models import Docente, Estudiante, Grado, Consulta, Materia, Docentemateria, Estudiantegrado
from django.contrib.auth import authenticate, login


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'edad', 'email', 'sexo']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'edad', 'email', 'sexo']


class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['grado']


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['grado', 'estudiante']


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['materia']


#crear docente materia
class DocentemateriaForm(forms.ModelForm):
    class Meta:
        model = Docentemateria
        fields = ['docente', 'materia']


#crear estudiante grado
class EstudiantegradoForm(forms.ModelForm):
    class Meta:
        model = Estudiantegrado
        fields =['estudiante', 'grado']