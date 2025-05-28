from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects.all().order_by('-start_date')
    return render(request, 'experience/home.html', {'jobs': jobs})
