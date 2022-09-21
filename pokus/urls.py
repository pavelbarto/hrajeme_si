from django.conf.urls.defaults import *

urlpatterns = patterns('hrajeme_si',
    (r'^time/$', 'pokus.views.current_time'),
)