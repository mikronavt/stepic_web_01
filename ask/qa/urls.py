__author__ = 'User'
from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'(^$)', 'qa.views.questions_all'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$', 'qa.views.test'),
    url(r'^question/(?P<qid>\w+)/$', 'qa.views.question_details', name='question_details'),
    url(r'^ask/.*$', 'qa.views.ask'),
    url(r'^popular/.*$', 'qa.views.popular_list'),
    url(r'^new/.*$', 'qa.views.test'),
    url(r'^answer/.*$', 'qa.views.answer'),
)
