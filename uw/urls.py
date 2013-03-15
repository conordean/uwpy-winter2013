# from django.conf.urls.defaults import *
from django.conf.urls import *

urlpatterns = patterns('uw.views',
    url(r'^$', 'list_activities'),
    url(r'^create$', 'create_activity'),
    url(r'^add$', 'add'),
    url(r'^lookup/$', 'lookup'),
    url(r'^(?P<program_id>\d+)','get'),
    # (r'^profile$', 'show_profile'),
    # (r'^profile/update$', 'update_profile'),
)
