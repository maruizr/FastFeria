from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electornico')
        usuario = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombres = nombres
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,username,email,nombres,password):
        usuario = self.create_user(
            email = email, 
            username = username, 
            nombres = nombres,
            password = password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario



class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo electronico', max_length=254, unique=True)
    nombres = models.CharField('Nombres', max_length=200, blank= True, null= True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null= True)
    imagen = models.ImageField('Imagen de perfil', upload_to ='perfil/', max_length=200, blank= True, null = True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()
    roles = (('productor','Productor'),('interno','Interno'),('externo','Externo'),('consultor','Consultor'),('transportista','Transportista'))
    tipo_usuario = models.CharField(max_length=50,choices=roles,default='productor')


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres']

    def __str__(self):
        return f'Usuario {self.username}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
