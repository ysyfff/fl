from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from files import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fl.views.home', name='home'),
    # url(r'^fl/', include('fl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^files/', include('files.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
