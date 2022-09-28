from email.policy import default
from django.db import models
from profile_owner import models as profile_owner_models
from django.conf import settings
from django_countries.fields import CountryField

class Chess_Instructor_Profile(models.Model):
    profile_owner = models.ForeignKey(profile_owner_models.Profile_owner, on_delete=models.CASCADE)
    title= models.CharField(max_length=16, blank=True, null=True)
    description=models.TextField(default='', blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="user"
    )
    country = CountryField(blank_label='(select country)',blank=False, null=True)

    chess_top_rating = models.IntegerField(default=0, blank=True)
    chess_top_rating_type= models.CharField(max_length=16, blank=True, default='') # in the future seperate table
    chess_top_rating_date= models.CharField(max_length=16, blank=True, default='')

    chess_actual_rating = models.IntegerField(default=0, blank=True)
    chess_actual_rating_type= models.CharField(max_length=16, blank=True, default='') # in the future seperate table

    # social media links
    fide_com = models.URLField(default='')
    facebook = models.URLField(default='')
    youtube = models.URLField(default='')
    instagram = models.URLField(default='')
    twitter = models.URLField(default='')
    lichess = models.URLField(default='')
    chess_com = models.URLField(default='')
    tiktok = models.URLField(default='')

    accepts_new_students = models.BooleanField(default=False)
    languages = models.CharField(max_length=16, blank=True, default='eng')

    profile_is_active = models.BooleanField(default=False)
    hidden_message = models.TextField(default='')

    # desc2 = models.TextField(default='')