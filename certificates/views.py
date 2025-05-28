from django.shortcuts import render
from .models import Certificate

def home(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates/home.html', {'certificates': certificates})
