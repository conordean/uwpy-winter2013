from django.conf.urls import patterns, include, url
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'views.index'),
    url(r'^appengine_sessions/', include('appengine_sessions.urls')),
    # url(r'^$', 'django.views.generic.simple.redirect_to', {'url': '/uw/', }),
    url(r'^home/', 'uw.views.home'),
    url(r'^profile/', include('userprofile.urls')),
    url(r'^program/?', include('uw.urls')),
    url(r'^account/', include('gaeauth.urls')),
    url(r'^invalid', 'django.views.generic.simple.direct_to_template',{'template':'invalid.html'}),
    url(r'^admin/', include(admin.site.urls)),
)
