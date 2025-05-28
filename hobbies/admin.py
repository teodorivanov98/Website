

from django.contrib import admin
from .models import Hobby

admin.site.register(Hobby)

class HobbiesAdmin(admin.ModelAdmin):
    exclude = ('Description',)

