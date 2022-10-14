from django.contrib import admin

# Register your models here.
from .models import client
class clientAdmin(admin.ModelAdmin):
    list_display = ('client_First_name', 'client_lname','client_address','client_dobdate','client_email','client_contact')
# Register your models here.


admin.site.register(client,clientAdmin)