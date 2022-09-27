from django.contrib import admin
from . import models

class Chess_Instructor_ProfileAdmin(admin.ModelAdmin): # he also write _UserAdmin
    list_display= (
        "user",
        "profile_owner",
        "title",
        "description"
    )
    fields =(
        "user",
        "profile_owner",
        "title",
        "description"
    )

admin.site.register(models.Chess_Instructor_Profile, Chess_Instructor_ProfileAdmin)