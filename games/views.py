from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'games/home.html')
def tictactoe(request):
    return render(request, 'games/tictactoe.html')

def rps(request):
    return render(request, 'games/rps.html')

def guess_animal(request):
    return render(request, 'games/guess_animal.html')