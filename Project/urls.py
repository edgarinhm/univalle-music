from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#urlpatterns = patterns('',
#     (r'^univalle-music/$', views.index),
#     (r'^subir-musica/$', views.subir_canciones),
#     (r'^web-report/$', views.web_reportes),
#     (dajaxice_config.dajaxice_url, include('dajaxice.urls')),     
#)

urlpatterns = patterns('',
(r'^$', include('uv_music.urls')),
(r'^univalle-music/', include('uv_music.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() #this servers static files and media files.
    #in case media is not served correctly
    urlpatterns += patterns('',
        (r'^univalle-music/media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )

#urlpatterns = patterns('',
#    (r'^view1/$', requires_login(my_view1)),
#    (r'^view2/$', requires_login(my_view2)),
#    (r'^view3/$', requires_login(my_view3)),
#)