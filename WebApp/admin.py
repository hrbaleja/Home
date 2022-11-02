from django.contrib import admin

# Register your models here.
from .models import Customer, Topic ,ourservice,ourArea,Contactus



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','First_name', 'Last_name','Address','DOB','Email','Contact')
admin.site.register(Customer,CustomerAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id','Title')
admin.site.register(Topic,TopicAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'image','people','discount','price','lista','listb','listc','listd','liste')
admin.site.register(ourservice,ServiceAdmin)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id','Title', 'image','Category','Group','Time')
admin.site.register(ourArea,AreaAdmin)

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('id','Topic', 'First_Name','Last_Name','Email','Contact','Message')
admin.site.register(Contactus,ContactusAdmin)