from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Register/', views.user_registration, name='registration'),
    path('Login/', views.user_login, name='login'),
    path('Logout/', views.user_logout, name='logout'),
    path('poll/', views.poll_question, name='poll_question'),
    path('vote_now/<str:slug>/', views.vote_now, name='vote_now'),
    path('vote', views.vote, name='vote'),
    path('poll_result/<int:id>/', views.display_result, name='result'),
]