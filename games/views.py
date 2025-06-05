from django.shortcuts import render
import random

def home(request):
    return render(request, 'games/home.html')

def tictactoe(request):
    return render(request, 'games/tictactoe.html')

def rock_paper_scissors(request):
    result = ""
    user_choice = request.GET.get("choice")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if user_choice:
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
        else:
            result = "Computer wins!"

    context = {
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    }
    return render(request, "games/rps.html", context)

def roll_dice(request):
    return render(request, 'games/roll_dice.html')
