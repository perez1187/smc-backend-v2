from profile_owner import models as profile_owner_models
from rest_framework import response, status

def chess_instructor_validation(data, request_user):
    try:
        profile_owner_models.Profile_owner.objects.get(user=data['user'],profile_type=data["profile_type"]).first()
        return response.Response({"error":"instructor exist"}, status=status.HTTP_400_BAD_REQUEST)
    except:
        pass