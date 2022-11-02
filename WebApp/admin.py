from django.contrib import admin

# Register your models here.
from .models import Customer, Topic ,Service



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','First_name', 'Last_name','Address','DOB','Email','Contact')
admin.site.register(Customer,CustomerAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id','Title')
admin.site.register(Topic,TopicAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'image','people','discount','price','lista','listb','listc','listd','liste')
admin.site.register(Service,ServiceAdmin)