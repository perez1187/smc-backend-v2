from rest_framework import serializers
from .models import UploadVideo


class VideoSerializer(serializers.ModelSerializer):
    
    link = serializers.CharField(max_length=255)
    class Meta:
        model = UploadVideo
        fields = ('__all__')
        extra_kwargs = {
            'link': {'required': True},
            'name': {'required': True}
            } 