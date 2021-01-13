'''
Created on Oct 22, 2012

@author: edgar
'''
from mutagen.easyid3 import EasyID3
import mutagen.id3

class Cancion(object):
    
    def __init__(self):
        self.ruta = ""
        self.trackNumber = ""
        self.artist = ""
        self.title = ""
        self.album = ""
        self.audioFile = ""
        self.metadatos = ""
        self.usuario = ""
    
     
    def getTitulo(self):
        return self.title
    
    def getAlbum(self):
        return self.album
    
    def getArtista(self):
        return self.artist
    
    def getNumeroPista(self):
        return self.trackNumber
    
    def getAudioFile(self):
        return self.audioFile
    
    def getRuta(self):
        return self.ruta
    
    def getUsuario(self):
        return self.usuario
    
    def getMetaDatos(self):
        return self.metadatos
    
    def setTitulo(self, titulo):
        self.title = titulo
        
    def setAlbum(self, album):
        self.album = album
        
    def setArtista(self, artista):
        self.artist = artista
    
    def setNumeroPista(self, pista):
        self.trackNumber = pista
        
    def setAudioFile(self, audioFile):
        self.audioFile = audioFile
        
    def setRuta(self, ruta):
        self.ruta = ruta
        
    def setMetaDatos(self, ruta):        
        try: 
            self.metadatos = EasyID3(ruta)
            print self.metadatos         
        except mutagen.id3.error:
            print "no paso"
           
    def setDefaulMeta(self):
        if  'title' not in self.metadatos.keys():
            self.metadatos['title'] = self.title
            self.metadatos['artist'] = u" "
            self.metadatos['album'] = u" "
            self.metadatos['tracknumber'] = u" "                        
        elif 'artist' not in self.metadatos.keys():
            self.metadatos['artist'] = u"ar"                     
        elif 'album' not in self.metadatos.keys():
            self.metadatos['album'] = u"al"
        elif 'tracknumber' not in self.metadatos.keys():
            self.metadatos['tracknumber'] = u"tr"
        self.metadatos.save()            
        print self.metadatos
            
    def setUsuario(self, usuario):
        self.usuario = usuario
        