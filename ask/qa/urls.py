from django.conf.urls import include, url

from django.urls import path

urlpatterns = [
    path(r'^login/.*$', 'qa.views.login', name='login'),
    path(r'^signup/.*$', 'qa.views.signup', name='signup'),
    path(r'^question/(?P<id>\d+)/.*$', 'qa.views.question', name='question'),
    path(r'^ask/.*$', 'qa.views.ask', name='ask'),
    path(r'^answer/.*$', 'qa.views.answer', name='answer'),
    path(r'^popular/.*$', 'qa.views.popular', name='popular'),
    path(r'^new/.*$', 'qa.views.new', name='new'),
    path(r'^logout/.*$', 'qa.views.logout', name='logout'),
    path(r'^$', 'qa.views.home', name='home')
]
