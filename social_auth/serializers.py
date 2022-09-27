import os
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from . import google
from .register import register_login_social_user

from decouple import config

class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):

        # validate token:
        user_data = google.Google.validate(auth_token)
        # sub - user id
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        # aud - my id
        if user_data['aud'] != config('GOOGLE_TEST_ID'):

            raise AuthenticationFailed('oops, who are you?')


        email = user_data['email']
        provider = 'google'


        user = register_login_social_user(provider=provider,email=email)
        return user
 