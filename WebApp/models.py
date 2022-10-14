from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class client(models.Model):  
    client_First_name = models.CharField(max_length=100)  
    client_lname = models.CharField(max_length=100)
    client_address = models.CharField(max_length=100)  
    client_dobdate = models.DateField()
    client_email = models.EmailField()
    client_password = models.CharField(max_length=100)  
    client_contact = models.CharField(max_length=15) 

    
    class Meta:  
        db_table = "client" 