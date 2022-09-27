from django.contrib.auth import authenticate
from authentication.models import User
from decouple import config
from rest_framework_simplejwt.tokens import RefreshToken

def register_login_social_user(provider, email):

    '''
        if user exist -> send access and refresh tokens
        if user doesnt exist -> create account and send tokens
    '''

    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        user = User.objects.get(email=email)
        refresh_token = RefreshToken.for_user(user)
        access_token = RefreshToken.for_user(user).access_token

        tokens = {
            "refresh":str(refresh_token),
            "access":str(access_token)
        }

        return {
            'email': email,
            'tokens': tokens
        }

    else:
        # create a new user
        user = {
            'email': email,
            'password': config('GOOGLE_TEST_ID')}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        # login new user
        new_user = authenticate(
            email=email, password=config('GOOGLE_TEST_ID'))
   
        return {
            'email': new_user.email,
            'tokens': new_user.tokens()
        }


