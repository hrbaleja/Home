
from unicodedata import name
from django.contrib import admin
from django.urls import path
from WebApp import views


urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.About, name='About'),
  path('contact', views.Contact, name='Contact'),
  path('service', views.Service, name='Service'),
  path('area', views.Area, name='Area'),
  path('login', views.u_login, name='login'),
  path('logout', views.logoutUser,name="logout"),
  path('office', views.office,name="office"),
  path('client', views.client,name="client"),
  path('register',views.register, name = 'register') ,
  path('info', views.info, name='info'),

  path('emp', views.emp),  
  path('showme',views.showme,name = 'showme'),  
  path('edit/<int:id>', views.edit),  
  path('update/<int:id>', views.update),  
  path('delete/<int:id>', views.destroy),
  path('Brochure', views.Brochure,name='Brochure')
  
 
    
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)