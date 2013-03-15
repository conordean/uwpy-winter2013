from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   url(r'^login/$', 'gaeauth.views.login', name='google_login'),
   url(r'^logout/$', 'gaeauth.views.logout', name='google_logout'),
   url(r'^authenticate/$', 'gaeauth.views.authenticate', name='google_authenticate'),
)
