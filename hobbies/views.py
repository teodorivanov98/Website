from django.shortcuts import render
from .models import Hobby

def home(request):
    hobbies = Hobby.objects.all()
    return render(request, 'hobbies/home.html', {'hobbies': hobbies})
