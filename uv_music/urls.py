from django.conf.urls import patterns, url

    
urlpatterns = patterns('uv_music.views',
# mustra la pagina de inicio
url(r'^$','index', name ='uv_music_inicio'),
# muestra el home del usuario
url(r'^home/$','log_in', name = 'uv_music_home'),
# muestra el formulario de ingreso
url(r'^login/$','index', name = 'uv_music_login'),
# muestra el formulario de registro
url(r'^registro/$','form_registro', name = 'uv_music_registro'),
#url(r'^registro/validar/$','uv_music_registro'),
#url(r'^registro/registrar/$','uv_music_registro'),
url(r'^subir/$','subir_audio', name = 'uv_music_audio'),
url(r'^stream/$','stream_audio', name = 'uv_music_stream'),
url(r'^404/$','error_404', name = 'uv_music_404'),
url(r'^500/$','error_500', name = 'uv_music_500'),
)

