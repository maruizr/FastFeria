from django import forms
from .models import VentLocal

class FormularioVentaLocal(forms.ModelForm):

    class Meta:
        model = VentLocal
        fields = ('nom_cli', 'ape_cli', 'email', 'direc_cli','num_calle', 'region', 'comuna')
        widgets ={
            'nom_cli': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre de cliente'
                }
            ),
            'ape_cli': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Apellido del Cliente'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos'
                }
            ),
            'direc_cli': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario'
                }
            ),
            'num_calle': forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'comuna': forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            
        }