from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('', views.new_questions, name='new_question'),
    path('login/', views.my_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:id>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.new, name='new'),
]
