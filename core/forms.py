from django import forms
from .models import Docente
from django.contrib.auth import authenticate, login

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields=['nombre', 'apellido', 'edad', 'email', 'sexo']