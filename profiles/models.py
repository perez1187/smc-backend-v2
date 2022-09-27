from email.policy import default
from django.db import models
from profile_owner import models as profile_owner_models
from django.conf import settings

class Chess_Instructor_Profile(models.Model):
    profile_owner = models.ForeignKey(profile_owner_models.Profile_owner, on_delete=models.CASCADE)
    title= models.CharField(max_length=16, blank=True, null=True)
    description=models.TextField(default='', blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="user"
    )