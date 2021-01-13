from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from clases.beans.Usuario import Usuario
from clases.util.Reportes import Reportes
from clases.persistencia.FachadaDB import FachadaDB
from clases.persistencia.UsuarioDao import UsuarioDao
from clases.beans.Cancion import Cancion
from clases.persistencia.CancionDao import CancionDao
import pickle
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import simplejson

def index(request):    
    return render_to_response('uv_music/index.html', locals(), context_instance=RequestContext(request))

def web_reportes(request):    
    response = HttpResponse(mimetype='application/pdf')
    reporte = Reportes()    
    reporte.generarPdf(response)    
    return response

def log_in(request):
    if request.method == 'GET':
        if request.session['logged'] == True:
            return render_to_response('uv_music/home.html', locals(), context_instance=RequestContext(request))
        else:
            return render_to_response('uv_music/404.html')
            
    elif request.method == 'POST':
        accion = request.POST['accion']    
        if accion == 'ingresar':
            nombre = request.POST['nombre']
            contrasena = request.POST['password']
            usuario = Usuario(nombre, contrasena)
            db = FachadaDB()
            usuarioDao = UsuarioDao(db)
            usuarioValido = usuarioDao.validarUsuario(usuario)
#        usuario = Usuario.objects.get(nombreUsuario="edgar")      
            if usuarioValido != None:
                request.session['logged'] = True
                serialized_user = pickle.dumps(usuarioValido)
                request.session['usuario'] = serialized_user
                return render_to_response('uv_music/home.html', locals(), context_instance=RequestContext(request))
            else:
                return  HttpResponseRedirect((reverse('uv_music_login')))    
        else:
            return HttpResponseRedirect((reverse('uv_music_404')))

def subir_audio(request):
    if request.method == 'GET':
        return render_to_response('uv_music/404.html')
    else:
        if request.method == 'POST':
            if request.session['logged'] == True:
                accion = request.POST['accion']
                if accion == 'subir_audio':
                    serialized_user = request.session['usuario']
                    usuario = pickle.loads(serialized_user)
                    canciones = []
                    for audioFile in request.FILES.getlist('audio'):        
                        cancion = Cancion()
                        cancion.setTitulo(audioFile.name)
                        cancion.setAudioFile(audioFile.read())
                        cancion.setRuta(usuario.getEmail()+'\\'+cancion.getTitulo())
                        cancion.setUsuario(usuario.getId())
                        #cancion.getRuta().replace('\\','/')
                        canciones.append(cancion)        
        
                        db = FachadaDB()
                        cancionDao = CancionDao(db)
                        resultado = cancionDao.guardarCancion(canciones)
                        if resultado == "exito":
                            return render_to_response('uv_music/home.html', locals(), context_instance=RequestContext(request))
                        else:
                            return HttpResponseRedirect((reverse('uv_music_500')))
                else:
                    return HttpResponseRedirect((reverse('uv_music_404')))       
            else:
                return HttpResponseRedirect((reverse('uv_music_404')))            
        else:
            return HttpResponseRedirect((reverse('uv_music_404')))    
    
def stream_audio(request):
##    The FileWrapper will turn the file object into an           
##    iterator for chunks of 8KB.  
#    resp = HttpResponse(FileIterWrapper(open('/.../test.mp3', "rb")), mimetype='audio/mpeg')  
#    resp['Content-Length'] = os.path.getsize("/.../test.mp3")  
#    resp['Content-Disposition'] = 'filename=test.mp3'  
#    return resp
    if request.is_ajax():
        if request.session['logged'] == True:
            accion = request.POST['accion']
            if accion == 'stream_audio':
                serialized_user = request.session['usuario']
                usuario = pickle.loads(serialized_user)                    
                db = FachadaDB()
                cancionDao = CancionDao(db)    
                canciones = cancionDao.consultarCanciones(usuario)
                json_canciones = cancionDao.to_json(canciones)    
                return HttpResponse(simplejson.dumps(json_canciones, cls=DjangoJSONEncoder),mimetype="application/json")
            else:
                return HttpResponseRedirect((reverse('uv_music_404')))
        else:
                return HttpResponseRedirect((reverse('uv_music_404')))
    else:
        return HttpResponseRedirect((reverse('uv_music_404')))
      
    
def form_login(request):
    return  HttpResponseRedirect((reverse('uv_music_login')))

@csrf_exempt
def form_registro(request):
#    return render_to_response('uv_music/registro.html', locals(), context_instance=RequestContext(request))
    if request.method == 'GET':
        return render_to_response('uv_music/registro.html', locals(), context_instance=RequestContext(request))
    else:       
        if  request.method == 'POST':
            accion = request.POST['accion']
            if accion == 'validarUsuario':
                emailUsuario = request.POST['email']
                db = FachadaDB()
                usuarioDao = UsuarioDao(db)
                validado = usuarioDao.buscarUsuario(emailUsuario)
                if validado == "existe":
                    return HttpResponse(validado)
                else:
                    return HttpResponse()    
            elif accion == 'registrarUsuario':
                nombre = request.POST['nombres']
                apellidos = request.POST['apellidos']
                email = request.POST['email']
                password = request.POST['password']
                telefono = request.POST['celular']
                operador = request.POST['operador']
        
                nuevoUsuario = Usuario(email, password)
                nuevoUsuario.setNombre(nombre)
                nuevoUsuario.setApellido(apellidos)
                nuevoUsuario.setTelefono(telefono)
                nuevoUsuario.setOperador(operador) 
                db = FachadaDB()
                usuarioDao = UsuarioDao(db)    
                registrado = usuarioDao.registrarUsuario(nuevoUsuario)    
    
                if registrado == "registrado":
                    return HttpResponseRedirect((reverse('uv_music_login')))
                else:
                    return render_to_response('uv_music/registro.html', locals(), context_instance=RequestContext(request))               
            else:
                return HttpResponseRedirect((reverse('uv_music_login')))
        else:
            return HttpResponseRedirect((reverse('uv_music_404')))

def log_out(request):
    del request.session['usuario']
    del request.session['logged']
    return HttpResponseRedirect((reverse('uv_music_login')))

def error_404(RequestContext):
    return render_to_response('uv_music/404.html')

def error_500(RequestContext):
    return render_to_response('uv_music/500.html')
