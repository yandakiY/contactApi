from django.contrib import admin
from contacts.models import Contact

# Register your models here.

@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
        pass