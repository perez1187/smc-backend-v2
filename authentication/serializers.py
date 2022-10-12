from dataclasses import fields
import email
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User

from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

# email reset
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        pass_err_mess= {
            'password':'password should be at least 6 characters long'
            }
        if len(password)<6:
            raise serializers.ValidationError(pass_err_mess)
        
        return attrs # so after validation we return attribuits
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ResendEmailActivation(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','password')
        extra_kwargs = {
            "id": {"read_only":True},
            "password": {"write_only": True}
        }

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68,write_only=True)
    # tokens = serializers.CharField(max_length= 68, read_only=True) # it return strings
    # it can be SerializerMethodField()
    # less problems on the frontend? https://www.youtube.com/watch?v=A0be-LPHxIc&list=PLx-q4INfd95EsUuON1TIcjnFZSqUfMf7s&index=20
    tokens = serializers.SerializerMethodField()


    def get_tokens(self, obj): # get_name (?)
        # print('objeccccccc',obj)
        user=User.objects.get(email=obj['email'])

        return {
            'access': user.tokens()['access'],
            'refresh':user.tokens()['refresh'] 
        }

    class Meta:
        model= User
        fields= ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user=auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('invalid credentials, try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email':user.email,
            'tokens': user.tokens
        }


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token= serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['token']

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']
    
class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True) 

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token':('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token') # or Validation Error

