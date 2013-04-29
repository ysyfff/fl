from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from files import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fl.views.home', name='home'),
    # url(r'^fl/', include('fl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^import/$', views.import_img),
    url(r'^export/$', views.export_fl),
    url(r'^pdf/$', views.export_pdf),
    url(r'^csv/$', views.export_csv),
    url(r'^xls/$', views.export_xls),
    url(r'^read/$', views.read_xls),
)
