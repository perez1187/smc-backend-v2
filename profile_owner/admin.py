from django.contrib import admin
from . import models

class ProfileOwnerAdmin(admin.ModelAdmin): # he also write _UserAdmin
    list_display= (
        "user",
        "profile_name",
        "slug",
        "profile_type",
        "link"
    )
    fields =(
        "user",
        "profile_name",
        "slug",
        "profile_type",
        "link"
    )

admin.site.register(models.Profile_owner, ProfileOwnerAdmin)

'''
example of other use

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'description')
    list_display=('id','name', 'location', 'description')

'''