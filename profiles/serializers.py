from rest_framework import serializers

#local
from .models import Chess_Instructor_Profile

# other apps
from profile_owner import models as profile_owner_models


class ChessInstructorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Chess_Instructor_Profile
        fields = ('id','title','description','profile_owner', 'user')

class CreateChessInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile_owner_models.Profile_owner
        fields = ('__all__')