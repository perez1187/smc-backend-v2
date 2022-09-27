from django.db import models

from django.conf import settings

PROFILE_TYPE = {
    'user_profile': 'user_profile', 
    'chess_instructor': 'chess_instructor',
    'checkers_instructor': 'checkers_instructor',
    }

class Profile_owner(models.Model):
    '''
        this is the way how django recommend to conect user as ForeignKey
    '''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="user"
    )
    profile_name = models.CharField(max_length=255, blank=True, null=True)
    slug= models.SlugField(blank=True, null=True)

    # added for auth provider, in future as db table
    profile_type = models.CharField(
        max_length=255, blank=False,
        null=False)
    link = models.CharField(max_length=255, blank=True, null=True)