from django import forms
from .models import VentLocal
from usuario.models import Usuario

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


class FormularioUsuario(forms.ModelForm):
    """ Formulario de registro de un usuario en la base de datos
    Variables:

        - password1: Contraseña
        - password2:  Verificar contraseña
    """

    password1 = forms.CharField(label = 'Contraseña',widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'requiered'
        }
    ))
    password2 = forms.CharField(label = 'Verificar ontraseña',widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Verifique su contraseña',
            'id':'password2',
            'required':'requiered'
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','username','nombres','apellidos','tipo_usuario')
        widgets ={
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo electronico'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario'
                }
            ),
            'tipo_usuario': forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
        }

    def clean_password2(self):
        # Validacion de la contraseña
        # Metodo que valida que ambas contraseñas sean iguales antes de ser encriptadas
        # Expeciones : ValidationError -- cuando las contraseñas no son iguales muestra un error
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

    def save(self, commit = True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data.get('password1'))
        if commit:
            usuario.save()
        return usuario