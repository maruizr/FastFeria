from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Usuarios, VentLocal


class AgregarUsuForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'
