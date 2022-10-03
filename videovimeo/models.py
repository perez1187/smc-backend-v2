from django.db import models
from django.conf import settings

# Create your models here.


class UploadVideo(models.Model):
    name = models.CharField(max_length=63, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    uri = models.CharField(max_length=63, blank=True, default='')
    status = models.CharField(max_length=63, blank=True, default='processing')
    
    # first it is a lokal link, and after upload it is vimeo link
    link=models.CharField(max_length=63, blank=False, default='')

    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)