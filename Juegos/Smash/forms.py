from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario
from .models import Image

class PerfilUsuarioForm(forms.ModelForm):
    class Meta():
        model = PerfilUsuario
        fields = ('foto_perfil',)

        #Remplaza el nombre de foto_perfil con el indicado en labels
        labels = {
            'foto_perfil' : 'Foto de Perfil'
        }

class ImagenForm(forms.ModelForm):
    class Meta():
        model = Image
        fields = ('nombre', 'imagen')
        labels = {
            'nombre' : 'Titulo',
            'imagen' : 'Imagen'
        }
        
        error_messages = {
            'nombre' : {
                'max_length': 'Maximo 150 caracteres',
                'required': 'Requerido'
            },
            'imagen' : {
                'required': 'Requerido'
            },
        }

    def __init__(self, *args, **kwargs):
        super(ImagenForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagen'].widget.attrs.update({'class': 'form-control'})


class RegistrarForm(forms.ModelForm):
    #cambia a password input en vez de charfield para que se oculte la contraseña al escribirla
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        #Remplazar los nombres de los fields con las labels que queramos
        labels = {
            'username' : 'Nombre de Usuario',
            'email' : 'Correo',
            'password' : 'Contraseña'
        }

        #Ingresar textos de ayuda para llenado
        help_texts = {
            'username' : '',
        }

        #mensajes de error
        error_messages = {
            'username' : {
                'max_length': 'Maximo 150 caracteres',
                'required': 'Requerido'
            },
            'password' : {
                'required': 'Requerido'
            },
        }

    #Constructor del formulario , le cambiamos la clase a form-control
    def __init__(self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        
