from django.db import models

# Create your models here.


class UploadVideo(models.Model):
    name = models.CharField(max_length=63, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    uri = models.CharField(max_length=63, blank=True, default='')
    status = models.CharField(max_length=63, blank=True, default='processing')
    link_lokal=models.CharField(max_length=63, blank=False, default='')