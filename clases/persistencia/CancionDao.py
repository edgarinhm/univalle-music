#from uv_music.models import Cancion
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from clases.beans.Cancion import Cancion
from MySQLdb.constants.FIELD_TYPE import STRING

class CancionDao(object):
    def __init__(self, db):
        self.db = db
    
    def guardarCancion(self,canciones):
        # Django ORM INSERT
        #=======================================================================
        # c = Cancion(
        #            tituloCancion = titulo,
        #            albumCancion = album,
        #            autorCancion = autor,
        #            numeroCancion = pista,
        #            usuario = user
        #            )
        # c.save()
        # c.audioFile.save(titulo, audio_file)
        #=======================================================================

#        prepared_query = []
        for cancion in canciones:        
            relative_path = default_storage.save(cancion.getRuta(), ContentFile(cancion.getAudioFile()))
#            prepared_query.append((cancion.getTitulo(),cancion.getAlbum(),cancion.getArtista(),cancion.getNumeroPista(),cancion.getUsuario(),''))
            
#           full path windows
            full_path = settings.MEDIA_ROOT +'\\'+ cancion.getRuta()        
            cancion.setMetaDatos(full_path)
            cancion.setDefaulMeta()
            cancion.setAlbum(cancion.getMetaDatos()['album'][0])
            cancion.setArtista(cancion.getMetaDatos()['artist'][0])
            cancion.setNumeroPista(cancion.getMetaDatos()['tracknumber'][0])
            sql="INSERT INTO uv_music_cancion (tituloCancion,albumCancion,autorCancion,numeroCancion,usuario_id,audioFile) VALUES ('%s', '%s', '%s', '%s', '%d', '%s')" % (cancion.getTitulo(),cancion.getAlbum(),cancion.getArtista(),cancion.getNumeroPista(),cancion.getUsuario(),relative_path)
            self.db.conectar()
            resultado = self.db.insertar(sql)
            self.db.cerrarConexion()
        if resultado!=None:               
            return resultado
        else:
            return "exito"
        
            
        
    def actualizarCancion(self, cancion, nuevos_datos):
        for dato in nuevos_datos:
            full_path = settings.MEDIA_ROOT +'\\'+ cancion.getRuta()
            cancion.setMetaDatos(full_path)
            cancion.getMetaDatos()['title']=dato['title']
            cancion.getMetaDatos()['artist']=dato['artist']
            cancion.getMetaDatos()['album']=dato['album']
            cancion.getMetaDatos()['tracknumber']=dato['tracknumber']
            cancion.getMetaDatos.save()
        
        # UPDATE WITH ORM DJANGO
        #=======================================================================
        # c = Cancion.objects.filter(tituloCancion=cancion.getTitulo())
        # c.tituloCancion = cancion.getTitulo()
        # c.albumCancion = cancion.getAlbum()
        # c.autorCancion = cancion.getAutor()
        # c.numeroCancion = cancion.getNumeroPista()         
        # c.save()
        #=======================================================================
        
    def consultarCanciones(self, usuario):
        sql = "SELECT tituloCancion, albumCancion, autorCancion, numeroCancion, audioFile FROM uv_music_cancion WHERE usuario_id = %d" % (usuario.getId())
        self.db.conectar()
        resultado = self.db.consultarTodos(sql)                        
        self.db.cerrarConexion()
        canciones = []
        if resultado != None:
            for row in resultado:
                cancion = Cancion()
                cancion.setTitulo(row[0])
                cancion.setAlbum(row[1])
                cancion.setArtista(row[2])
                cancion.setNumeroPista(row[3])
                # cambiando el path para windows                
                full_path = "http://localhost/media/" + row[4]
                cancion.setAudioFile(full_path)
                canciones.append(cancion)
            return canciones
        else:            
            return resultado
#       c = Cancion.objects.filter(usuario = usuario.getEmail())

    def to_json(self, canciones):
        json_response = []       
        for cancion in canciones:   
            typo = cancion.getTitulo()
            t = typo.split('.')
            if t[1]=='ogg':
                t[1]='oga'  
            elif t[1]=='mp4':
                t[1]='m4a'
            elif t[1]=='webm':
                t[1]='webma'            
            json = {
                    'title': cancion.getTitulo(),
                    'artist': cancion.getArtista(),
                    ""+t[1]: cancion.getAudioFile()
                    }
            json_response.append(json)            
        return json_response
    
    def eliminarCancion(self, cancion):
        sql = "DELETE FROM uv_music_cancion WHERE usuario_id = %d AND tituloCancion =%s" % (cancion.getUsuario(),cancion.getTitulo())
        self.db.conectar()
        resultado = self.db.consultarTodos(sql)                        
        self.db.cerrarConexion()
        if resultado != None:
            return resultado
        else:
            default_storage.delete(cancion.getAudioFile())
            return "eliminado"    
        