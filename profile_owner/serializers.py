import imp
from rest_framework import serializers

from .models import Profile_owner, UploadImageTest


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile_owner
        fields = ("__all__")
        #fields = ('id','profile_name','slug','user', 'link', "socials")

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('name', 'image')