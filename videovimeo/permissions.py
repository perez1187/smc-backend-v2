from rest_framework import permissions
from profile_owner.models import Profile_owner 

# custom permission
class UserIsCoach(permissions.BasePermission):
    message = 'You are not instructor'
    def has_permission(self, request, view):
        try:
            Profile_owner.objects.get(user= request.user,is_instructor=True)
        except:
            return False            

        return True
     

