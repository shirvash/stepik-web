from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<id>', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('answer/', views.answer, name='answer'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.new, name='new'),
    path('logout/', views.logout, name='logout'),

]
