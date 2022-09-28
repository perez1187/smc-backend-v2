from rest_framework import serializers,response

#local
from .models import Chess_Instructor_Profile

# other apps
from profile_owner import models as profile_owner_models
from django_countries.serializers import CountryFieldMixin
from profile_owner import models as profile_owner_models




class ChessInstructorSerializer(CountryFieldMixin,serializers.ModelSerializer):
    
    profile_owner_name=serializers.ReadOnlyField()
    user_name=serializers.ReadOnlyField()

    class Meta:
        model = Chess_Instructor_Profile
        fields = ('__all__')
        
        extra_kwargs = {
            "id": {"read_only":True},
            "user": {"read_only": True},
            "profile_owner": {"read_only": True},
            "country":{"country_dict":True}
        }

class CreateChessInstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = profile_owner_models.Profile_owner
        fields = ('id',"profile_name","slug","profile_type","link","user")



    def validate(self, attrs):
                        
        user_id = attrs.get('user','')
        profile_type = attrs.get('profile_type','')
        
        if profile_type != "chess_instructor":
            raise serializers.ValidationError({"error":"this is endpoint for chess instructor"})

        return attrs # so after validation we return attribuits

