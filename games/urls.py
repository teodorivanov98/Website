from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='games-home'),
    path('tictactoe/', views.tictactoe, name='tictactoe'),
    path('rps/', views.rps, name='rock-paper-scissors'),
    path('guess/', views.guess_animal, name='guess-animal'),
]