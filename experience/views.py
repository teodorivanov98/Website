from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # homepage
    path('experience/', include('experience.urls')),
    path('education/', include('education.urls')),
    path('certificates/', include('certificates.urls')),
    path('hobbies/', include('hobbies.urls')),
    path('contacts/', include('contacts.urls')),
    path('games/', include('games.urls')),
]
from django.shortcuts import render

def home(request):
    return render(request, 'experience/home.html')