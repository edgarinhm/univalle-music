import os
from django.db import models

def get_audio_path(self, filename):
    return os.path.join('musica',str(self.usuario.emailUsuario),filename)

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=200)
    apellidoUsuario = models.CharField(max_length=200)
    passwordUsuario = models.CharField(max_length=200)
    emailUsuario = models.EmailField(max_length=200) 
    telefonoUsuario = models.CharField(max_length=200)
    operadorUsuario = models.CharField(max_length=200)
    rolUsuario = models.BooleanField(default=False)
        
class Cancion(models.Model):
    tituloCancion = models.CharField(max_length=200)
    albumCancion = models.CharField(max_length=200)
    autorCancion = models.CharField(max_length=200)
    numeroCancion = models.CharField(max_length=200)    
    usuario = models.ForeignKey(Usuario,related_name='musica',on_delete=models.CASCADE)
    audioFile = models.FileField(upload_to=get_audio_path)
    
    
