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

class Customer(models.Model):  
    First_name = models.CharField(max_length=100)  
    Last_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)  
    DOB = models.DateField()
    Email = models.EmailField()
    password = models.CharField(max_length=50)  
    Contact = models.CharField(max_length=10) 

    class Meta:  
        db_table = "Customer" 
    def __str__(self):
        return self.First_name

class Topic(models.Model):  
    Title = models.CharField(max_length=100)     
    
    def __str__(self):
        return self.Title


class Service(models.Model):
    image=models.ImageField(upload_to='Dataimage', blank=True)
    title=models.CharField(max_length=100)
    people=models.CharField(max_length=10)
    discount=models.CharField(max_length=10)
    price=models.CharField(max_length=10)
    lista=models.CharField(max_length=100)
    listb=models.CharField(max_length=100)
    listc=models.CharField(max_length=100)
    listd=models.CharField(max_length=100,blank=True)
    liste=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title