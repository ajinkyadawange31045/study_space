from django.db import models

class Profile(models.Model):
    BRANCH_CHOICES = [
        ('ECE', 'ECE'),
        ('CSE', 'CSE'),
        ('Chemical', 'Chemical'),
        ('Mining', 'Mining'),
        ('IT', 'IT'),
        ('Mech', 'Mech'),
    ]
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=100)
    semester = models.IntegerField(max_length=8)
    about = models.TextField(max_length=244)
