import email
from rest_framework import generics, response, status, views
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings


# local
from .models import User
from .serializers import RegisterSerializer, UserSerializer, ChangePasswordSerializer, LoginSerializer, EmailVerificationSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer, LogoutSerializer, ResendEmailActivation
from .emails import send_register_email_sendgrid

# other apps
from profile_owner import models as profile_owner_models


# test
from rest_framework import permissions
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

# 3rd part
import jwt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# email reset
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    # renderer_classes = (UserRenderer,) # email act social media auth app

    def post(self, request):
        # save user to db
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        # create token for User      
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        # True for user has password (false if user create account by social media)
        user.is_password = True
        user.save()

        # sending registration email

        '''this is if I want to get domain'''
        #current_site = get_current_site(request).domain
        #relative_link=reverse('email-verify') # relative name urls.py
        # absurl = 'http://'+current_site +relative_link+"?token="+str(token)

        absurl = "http://localhost:5173/activate?token="+str(token)+"&email="+user_data["email"]
        
        print("absurl: ",absurl)
        
        data = {
            "receiver":user_data["email"],
            "domain":absurl,
            "subject": 'Verify Email',
        }

        # sending email from sendgrid
        send_register_email_sendgrid(data) # manualy set receiver o.perez1187@gmail.com

        # create profile owner
        profile_owner_models.Profile_owner(user=user, profile_type='user_profile').save()



        return response.Response(user_data, status=status.HTTP_201_CREATED)

class ResendEmailActivationView(generics.GenericAPIView):
    '''
        if token is expired
        user account is not activate
        create new Token and send new Email
    '''
    serializer_class = ResendEmailActivation
    def post (self, request):
        print(request.data)
        # serializer= self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user_data = serializer.data

        # print("user_data", user_data)

        # create token for User
        try:       
            user = User.objects.get(email=request.data['email'])
        except:
            return response.Response({"error":"user does not exist"})
        print("user: ", user)
        print("user is verified", user.is_verified)
        if user.is_verified == False :
            
            token = RefreshToken.for_user(user).access_token
            # print("tokent", token, ' is verified', user.is_verified)

            # sending another activation email
            absurl = "http://localhost:5173/activate?token="+str(token)

            data = {
                "receiver":request.data["email"],
                "domain":absurl,
                "subject": 'Verify Email',
            }

            # sending email from sendgrid
            send_register_email_sendgrid(data) # manualy set receiver o.perez1187@gmail.com
            return response.Response({"message": "email sent"})
        
        else :
            return response.Response({"message": "your account is already activated"})

        

class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description my', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config]) # create data for swagger
    def get(self,request):
        token = request.GET.get('token') # take token from url

        # try to decode, secret key from settings (this projet secret key)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user=User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return response.Response({'email':'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return response.Response({'error':'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return response.Response({'error':'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
'''
    Get User info
'''
class MeAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user # that give us email from token ?
        print('user: ',user)
        return User.objects.filter(email=user) # is owner of user account

'''
    this works for havinng id
'''
class UserAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"


    def get_queryset(self):

        # print ('self:   ',self)
        user = self.request.user # that give us email from token ?
        # print('user: ',user)
        return User.objects.filter(email=user)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            # print(obj)
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)


            if serializer.is_valid():
                # Check old password
                user=auth.authenticate(email=self.object, password=serializer.data.get("old_password"))

                if not user:
                    raise AuthenticationFailed('invalid credentials, try again')                
                
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
    forget password
    1. User request new password and we send an email with link
    2. User open email and click link, we check is token is valid
    3. if we yes, im_verifid = True

    for mobile https://www.youtube.com/watch?v=foYq1MGS4wA&list=PLx-q4INfd95EsUuON1TIcjnFZSqUfMf7s&index=24
'''

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):

        # serializer = self.serializer_class(data=data)
        # serializer.is_valid(raise_exception=True)

        # manually validation
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            # here will send an email
            user= User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            # # sending registration email

            current_site = get_current_site(request=request).domain
            relative_link=reverse('password-reset-confirm',kwargs={'uidb64':uidb64,'token':token}) # relative name urls.py
            absurl = 'http://'+current_site +relative_link
            
            email_body = 'hi' # I use template
            print (absurl)

            data = {
                "receiver":email,
                "domain":absurl,
                "subject": 'Verify Email',
            }
            # send email with password reset link
            # reset_pass_sendgrid(data)
            return response.Response({'success':'We have sent you a link to reset pas'},status=status.HTTP_200_OK)
        return response.Response({'error':'Emaiil not exist'},status=status.HTTP_400_BAD_REQUEST)
        


class PasswordTokenCheckAPI(generics.GenericAPIView):

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64)) #that give us the user
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                return response.Response({"error":"Token is not vali, please request a new one"})            

            return response.Response({'success': True, 'message':'Credentials Valid','uidb64':uidb64,'token':token},status=status.HTTP_200_OK )


        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return response.Response({"error":"Token is not vali, please request a new one"})

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    
    '''
        we put refresh token on blacklist
        for delete black listed tokens from db
        python manage.py flushepiredtokens
    '''
    
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)        
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)