from django.contrib import admin
from . import models

class ProfileOwnerAdmin(admin.ModelAdmin): # he also write _UserAdmin
    list_display= (
        "id",
        "user",
        "is_instructor",
        "avatar",
        'first_name',
        'last_name',
        "profile_name",
        "slug",
        "profile_type",
        "socials",
        "chess_profile",
        "checkers_profile",
        "profile_is_active",
        "hidden_message",
        "accepts_new_students",
        "languages",
        


    )
    fields =(
        
        "user",
        "is_instructor",
        "avatar",
        'first_name',
        'last_name',
        "profile_name",
        "slug",
        "profile_type",
        "socials",
        "chess_profile",
        "checkers_profile",
        "profile_is_active",
        "hidden_message",
        "accepts_new_students",
        "languages",
        "languages_test",
        

    )

admin.site.register(models.Profile_owner, ProfileOwnerAdmin)
admin.site.register(models.Languages)
admin.site.register(models.UploadImageTest)

'''
example of other use

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'description')
    list_display=('id','name', 'location', 'description')


    first_name = models.CharField(max_length=65, blank=True, default="")
    last_name = models.CharField(max_length=65, blank=True, default="")
    profile_name = models.CharField(max_length=255, blank=True, default="")
    slug= models.SlugField(blank=True, null=True,unique=True)

    # added for auth provider, in future as db table
    profile_type = models.CharField(
        max_length=255, blank=False,
        null=False)
    
    # link = models.CharField(max_length=255, blank=False, default="")

    socials = models.JSONField(default=default_socials)
    chess_profile = models.JSONField(default=default_chess_profile)
    profile_is_active = models.BooleanField(default=False)
    hidden_message = models.TextField(default='')
    accepts_new_students = models.BooleanField(default=False)
    languages = models.CharField(max_length=16, blank=True, default='eng')
'''