from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'songfable.views.home', name='home'),
    # url(r'^songfable/', include('songfable.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
