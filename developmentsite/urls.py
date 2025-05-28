from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('experience/', include('experience.urls')),
    path('education/', include('education.urls')),
    path('certificates/', include('certificates.urls')),
    path('hobbies/', include('hobbies.urls')),
    path('contacts/', include('contacts.urls')),
    path('games/', include('games.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
