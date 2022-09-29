from rest_framework import generics,views,status,response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404

# local
from . serializers import ProfileSerializer, ImageSerializer
from . models import Profile_owner, UploadImageTest
from profile_owner import serializers



'''
    Get User info
'''
class ProfilesAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile_owner.objects.all()

class ProfilesFilteredAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    
    # examle: http://127.0.0.1:8000/profile-owner/profiles/?profile=user_profile&language=1
    def get_queryset(self):
        queryset = Profile_owner.objects.all()
        
        profile = self.request.query_params.get('profile')
        if profile is not None:        
            queryset=queryset.filter(profile_type=profile)
        language = self.request.query_params.get('language')
        if language is not None:        
            queryset=queryset.filter(languages_test=language)        
        return queryset



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
    permission_classes=(IsAuthenticatedOrReadOnly,)


    def get_queryset(self):
        user = self.request.user # that give us email from token ?
        print('user: ',user)
        return Profile_owner.objects.filter(user=user) # is owner of user account