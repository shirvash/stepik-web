from django.conf.urls import patterns, include, url

urlpatterns = [
    '', 
    url(r'^login/.*$', 'qa.views.login', name='login'),
    url(r'^signup/.*$', 'qa.views.signup', name='signup'),
    url(r'^question/(?P<id>\d+)/.*$', 'qa.views.question', name='question'),
    url(r'^ask/.*$', 'qa.views.ask', name='ask'),
    url(r'^answer/.*$', 'qa.views.answer', name='answer'),
    url(r'^popular/.*$', 'qa.views.popular', name='popular'),
    url(r'^new/.*$', 'qa.views.new', name='new'),
    url(r'^logout/.*$', 'qa.views.logout', name='logout'),
    url(r'^$', 'qa.views.home', name='home')
              ]
