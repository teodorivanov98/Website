from django.shortcuts import render
from .models import Education

def home(request):
    schools = Education.objects.all().order_by('-start_date')
    return render(request, 'education/home.html', {'schools': schools})
