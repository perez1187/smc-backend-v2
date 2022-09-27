from email.policy import default
from django.db import models
from profile_owner import models as profile_owner_models

class Chess_Instructor_Profile(models.Model):
    owner = models.ForeignKey(profile_owner_models.Profile_owner)
    title= models.CharField(max_lenght=16, blank=True, null=True)
    description=models.TextField(default='')