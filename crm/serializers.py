from rest_framework import serializers

from .models import Student, Students_note


class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("__all__")
        #fields = ('id','profile_name','slug','user', 'link', "socials")