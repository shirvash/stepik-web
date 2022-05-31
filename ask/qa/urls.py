from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import login
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    #path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:qu_id>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.new, name='new'),
    #path('answer/', views.answer, name='answer'),
    #path('logout/', views.logout_, name='logout'),
]
