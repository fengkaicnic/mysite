from django.conf.urls import patterns, include, url

from mysite.views import hello
from mysite.views import current_time
from mysite.views import current_datetime
from mysite.views import hours_ahead
from mysite.views import current
from mysite.views import display
from django.contrib import admin
admin.autodiscover()
from mysite.books import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^current/$', current_time),
    ('^curren/$', current),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^display/$', display),
    ('^search/$', views.search_form),
    ('^search-form/$', views.search),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
