from rest_framework import generics,views,status,response

# local
from . serializers import ProfileSerializer
from . models import Profile_owner
from profile_owner import serializers

'''
    Get User info
'''
class MyProfilesAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile_owner.objects.all()

    # def get_queryset(self):
    #     return Profile_owner.objects.filter(profile_type="chess_instructor")

    # def get_queryset(self):
    #     user = self.request.user # that give us email from token ?
    #     print('user: ',user)
    #     return Profile_owner.objects.filter(user=user) # is owner of user account

class ProfilesFilteredAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    
    # http://127.0.0.1:8000/profile-owner/profiles/?profile=chess_instructor
    def get_queryset(self):
        queryset = Profile_owner.objects.all()
        profile = self.request.query_params.get('profile')
        
        queryset=queryset.filter(profile_type=profile)
        
        return queryset



