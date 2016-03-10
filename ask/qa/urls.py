__author__ = 'User'
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', 'test'),
    url(r'^login/', 'test'),
    url(r'^signup/', 'test'),
    url(r'^question/(\d+)/', 'test'),
    url(r'^ask/', 'test'),
    url(r'^popular/', 'test'),
    url(r'^new/', 'test'),
)
