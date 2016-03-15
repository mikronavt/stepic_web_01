__author__ = 'User'
from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'(^$)', 'qa.views.questions_lists_all'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$', 'qa.views.test'),
    url(r'^question/?P<slug>\w+/$', 'qa.views.question'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'^popular/.*$', 'qa.views.popular'),
    url(r'^new/.*$', 'qa.views.test'),
)
