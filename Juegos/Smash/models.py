from django.db import models
from django.contrib.auth.models import User
from django import forms

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True)

    def __str__(self):
        return self.user.username

class Image(models.Model):
    nombre = models.CharField(max_length=500)
    imagen = models.FileField(upload_to='img', blank=True)

    def __str__(self):
        return self.nombre
