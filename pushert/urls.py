from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import pmessages.views

urlpatterns = patterns('',
    url(r'^$', pmessages.views.home, name='home'),  
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^pusher/', include('django_pusher.urls')),  
    (r'^accounts/', include('allauth.urls')),

 
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))