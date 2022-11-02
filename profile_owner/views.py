from rest_framework import generics,views,status,response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from django.shortcuts import get_object_or_404

# local
from . serializers import ProfileSerializer, ImageSerializer
from profile_owner import serializers

from authentication import authentication

#  models
from . models import Profile_owner, UploadImageTest
from authentication import models

'''
    create profile owner (eg chess instructor)
'''
class CreateProfileOwnerApiView(generics.GenericAPIView):
    queryset = Profile_owner.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # screating profile owner for chess instructor
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)  

        ''' verify user with self.request user  '''
        try: 
            currentUser = models.User.objects.get(id=request.data['user'])
        except:
            currentUser= 0
        
        
        if currentUser == self.request.user :
            # print(currentUser)
            # print(request.data['user'])
            # print(self.request.user)
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("current user !=  user in post method")
            return response.Response({"error":"current user !=  user in post method"}, status=status.HTTP_401_UNAUTHORIZED)
        

'''
    Get User info
'''
class ProfilesAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer  
    authentication_classes=(authentication.CustomUserAuthentication, )

    # queryset = Profile_owner.objects.all()
    def get_queryset(self):
        """
        This view should return a list of all the profiles
        for the currently authenticated user.
        """
        user = self.request.user

        print("user", user)
        # return Profile_owner.objects.all()
        return Profile_owner.objects.filter(user=user)

class ProfilesFilteredAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    
    # examle: http://127.0.0.1:8000/profile-owner/profiles/?profile=user_profile&language=1
    def get_queryset(self):
        queryset = Profile_owner.objects.all()
        queryset1 = Profile_owner.objects.filter(profileType=2, is_instructor=True) # id 2 is a chess instructor
        queryset2 = Profile_owner.objects.filter(profileType=3, is_instructor=True) # id 3 is a draughts instructor
        
        
        '''  temporary after that we add filtering '''
        profile = self.request.query_params.get('profile')
        language = self.request.query_params.get('language')

        ''' this is something that I need to check after adding filtering to fron'''
        # if profile is not none, we change queryset and we check language
        # after that we return queryset
        if profile is not None:        
            queryset=queryset.filter(profile_type=profile)
            
            if language is not None:        
                queryset=queryset.filter(languages_test=language) 
            return queryset
        
        if language is not None:        
            queryset=queryset.filter(languages_test=language)  
            return queryset
         
        ''' for returning more value we can use this:  '''      
        return queryset1 | queryset2



# class ImageViewSet(generics.ListAPIView):
#     queryset = UploadImageTest.objects.all()
#     serializer_class = ImageSerializer

#     def post(self, request, *args, **kwargs):
#         file = request.data['file']
#         image = UploadImageTest.objects.create(image=file)
        
#         return response.Response({'message': "Uploaded"}, status=status.HTTP_200_OK)
#         #return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

class ImageViewSet(views.APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': "Uploaded"}, status=status.HTTP_200_OK)

class ProfileAPIVIew(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile_owner.objects.all()
    lookup_field = "id"

class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile_owner.objects.all()
    lookup_field = "id"
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes=(IsAuthenticatedOrReadOnly,)


    def get_queryset(self):
        user = self.request.user # that give us email from token ?
        #print('user: ',user)
        return Profile_owner.objects.filter(user=user) # is owner of user account