from django.conf.urls import patterns
urlpatterns = patterns('image_service.views',
    (r'^upload/$', 'upload'),
    #(r'^display/(?P<key>.*)', 'display'),
    (r'^display/(?P<key>[0-9a-z_\-]+)/(?P<demension_x>[0-9]+)x(?P<demension_y>[0-9]+)(?P<process>[a-z]?)\.jpg', 'display')
)

