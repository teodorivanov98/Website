from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    exclude = ('message',)

admin.site.register(Contact, ContactAdmin)