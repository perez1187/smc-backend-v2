from rest_framework import serializers

from .models import Student, Students_note


class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("__all__")

class StudentNotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students_note
        fields = ("__all__")