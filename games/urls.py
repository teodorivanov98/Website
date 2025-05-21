from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='games-home'),
    path('tictactoe/', views.tictactoe, name='tictactoe'),
    path('rock-paper-scissors/', views.rock_paper_scissors, name='rock_paper_scissors'),
    path('guess-animal/', views.guess_animal, name='guess_animal'),
]
