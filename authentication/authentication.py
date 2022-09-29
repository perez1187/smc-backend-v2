from django.conf import settings
from rest_framework import authentication, exceptions
import jwt
from . import models

'''
info from https://stackoverflow.com/questions/15113248/django-tokenauthentication-missing-the-authorization-http-header
'''
class CustomUserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        # token = request.COOKIES.get("jwt") # not using [] because problem if there is no jwt?
        token = request.META.get('HTTP_AUTHORIZATION', None)
        # token = request.headers['Authorization'] # that will also work
        
        if not token:
            return None
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")
        
        user = models.User.objects.filter(id=payload["user_id"]).first()

        return (user, None)