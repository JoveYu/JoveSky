from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JoveSky.views.home', name='home'),
    # url(r'^JoveSky/', include('JoveSky.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve'
        ,{'document_root': settings.MEDIA_ROOT }),
)

urlpatterns += patterns('',
    (r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += patterns('',
    url(r'^', include('blog.urls')),
)

