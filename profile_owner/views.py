from rest_framework import generics,views,status,response

# local
from . serializers import ProfileSerializer
from . models import Profile_owner
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



