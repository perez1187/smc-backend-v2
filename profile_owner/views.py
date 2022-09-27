from rest_framework import generics

# local
from . serializers import ProfileSerializer
from . models import Profile_owner

'''
    Get User info
'''
class MyProfilesAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile_owner.objects.all()

    def get_queryset(self):
        user = self.request.user # that give us email from token ?
        print('user: ',user)
        return Profile_owner.objects.filter(user=user) # is owner of user account