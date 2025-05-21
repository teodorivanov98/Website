from django.shortcuts import render

def home(request):
    return render(request, 'games/home.html')

def tictactoe(request):
    return render(request, 'games/tictactoe.html')

def rock_paper_scissors(request):
    return render(request, 'games/rock_paper_scissors.html')

def guess_animal(request):
    return render(request, 'games/guess_animal.html')