from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'teramlapp.views.index'),
    url(r'^query$', 'teramlapp.views.query'),
    # Examples:
    # url(r'^$', 'teraml.views.home', name='home'),
    # url(r'^teraml/', include('teraml.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
