import imp
from rest_framework import serializers

from .models import Profile_owner


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile_owner
        fields = ('__all__')