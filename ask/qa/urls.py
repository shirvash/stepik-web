from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:qu_id>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.new, name='new'),
    #path('answer/', views.answer, name='answer'),
    #path('logout/', views.logout, name='logout'),

]
