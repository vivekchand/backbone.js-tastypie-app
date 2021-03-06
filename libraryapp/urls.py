from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from libraryapp.api import *
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(BookResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'libraryapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'libraryapp.views.index', name='index'),
)
