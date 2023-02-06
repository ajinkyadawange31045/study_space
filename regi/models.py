from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    BRANCH_CHOICES = [
        ('ECE', 'ECE'),
        ('CSE', 'CSE'),
        ('Chemical', 'Chemical'),
        ('Mining', 'Mining'),
        ('IT', 'IT'),
        ('Mech', 'Mech'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True,)
    phone_number = models.IntegerField(null=True, blank=True)
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=100,null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(default = 'user.jpg',upload_to='users/',null = True,blank=True)
    
    def __str__(self):
        return '%s %s' % (self.user.first_name,self.user.last_name)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()