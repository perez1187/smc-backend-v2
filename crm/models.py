from email.policy import default
from django.db import models
from django.conf import settings
from profile_owner.models import Profile_owner

# Create your models here.
class Student(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=65, blank=True, default='')
    description = models.TextField(default='', blank=True)
    instructor = models.ForeignKey(Profile_owner, on_delete=models.CASCADE)

class Students_note(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    note = models.TextField(default='', blank=True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    prize = models.DecimalField(max_digits=6, decimal_places=2, blank= True, default= 0)
    instructor = models.ForeignKey(Profile_owner, on_delete=models.CASCADE, blank=True,default=1) # deete default on production