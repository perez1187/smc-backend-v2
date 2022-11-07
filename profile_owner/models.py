from email.policy import default
from django.db import models

from django.conf import settings

PROFILE_TYPE = {
    'user_profile': 'user_profile', 
    'chess_instructor': 'chess_instructor',
    'checkers_instructor': 'checkers_instructor',
    }

def default_socials():
    return {
        "facebook":"",
        "instagram":"",
        "twitter":"",
        "youtube":"",
        "tiktok":"",
        "own_www":"",
    }
def default_chess_profile():
    return {
        "chess_title":"",
        "top_rating":"",
        "top_rating_date":"",
        "top_rating_type": "",
        "actual_rating":"",
        "actual_rating_type":"",
        "fide.com":"",
        "chess.com":"",
        "lichess.org":"",
    }
def default_checkers_profile():
    return {
        "draughts_title":"",
        "top_rating":"",
        "top_rating_date":"",
        "top_rating_type": "",
        "actual_rating":"",
        "actual_rating_type":"",
        "fmjd.org":"",        
    }

''' old function uploa  '''
# def avatar_upload(instance,filename):
#     return 'avatars/{filename}'.format(filename=filename)

def avatar_upload(instance,filename):
    return '/'.join(['profiles',str(instance.slug),'avatar',filename])

class Languages(models.Model):
    language = models.CharField(max_length=32, blank=True)

class ProfileType(models.Model):
    type = models.CharField(max_length=32, blank=True)

class Profile_owner(models.Model):
    '''
        this is the way how django recommend to conect user as ForeignKey
    '''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="user",
        # null=True,
        blank=True # temporary,
    
    )
    profileType = models.ForeignKey(ProfileType, on_delete= models.PROTECT, default=1)
    avatar= models.ImageField(upload_to=avatar_upload, blank=True, null=True)
    first_name = models.CharField(max_length=65, blank=True, default="")
    last_name = models.CharField(max_length=65, blank=True, default="")
    profile_name = models.CharField(max_length=255, blank=True, default="")
    slug= models.SlugField(blank=True, null=True,unique=True)

    country = models.CharField(max_length =5, blank= True, default="pl")

    is_instructor = models.BooleanField(default=False, blank=True)
   
    # added for auth provider, in future as db table
    # profile_type = models.CharField(
    #     max_length=255, blank=True,
    #     null=False)
    
    # link = models.CharField(max_length=255, blank=False, default="")

    socials = models.JSONField(default=default_socials, blank=True)
    chess_profile = models.JSONField(default=default_chess_profile,blank=True)
    checkers_profile = models.JSONField(default=dict,blank=True)
    profile_is_active = models.BooleanField(default=False,blank=True)
    hidden_message = models.TextField(blank=True,default='')
    accepts_new_students = models.BooleanField(default=False, blank=True)
    languages = models.CharField(max_length=16, blank=True, default='eng')

    languages_test = models.ManyToManyField(Languages, blank=True, null=True)

def nameFile(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class UploadImageTest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)