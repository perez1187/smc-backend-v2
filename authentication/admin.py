from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin): # he also write _UserAdmin
    list_display= (
        "id",
        "email",
    )

admin.site.register(models.User, UserAdmin)

'''
example of other use

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'description')
    list_display=('id','name', 'location', 'description')

'''