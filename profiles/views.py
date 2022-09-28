'''
1 create profile ownerchess instructor
2. check id
3.  create chess instructor profile
'''

from pkgutil import ImpImporter
from rest_framework import generics,response, status

# local
from . serializers import ChessInstructorSerializer, CreateChessInstructorSerializer
from . models import Chess_Instructor_Profile
from . utils import chess_instructor_validation
# other aps
from profile_owner import models as profile_owner_models
from django.conf import settings
from authentication import models as auth_models

'''
    Get User info
'''
class ChessInstructorAPIView(generics.ListAPIView):
    serializer_class = ChessInstructorSerializer
    queryset = Chess_Instructor_Profile.objects.all()

    def get_queryset(self):
        user = self.request.user # that give us email from token ?
        print('user: ',user)
        return Chess_Instructor_Profile.objects.filter(user=user) # is owner of user account

'''
    this works for havinng id
'''
class ChessInstructorAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChessInstructorSerializer
    queryset = Chess_Instructor_Profile.objects.all()
    lookup_field = "id"


    def get_queryset(self):

        # print ('self:   ',self)
        user = self.request.user # that give us email from token ?
        # print('user: ',user)
        return Chess_Instructor_Profile.objects.filter(user=user)


class CreateChessInstructorAPIView(generics.GenericAPIView):

    serializer_class = CreateChessInstructorSerializer
    # renderer_classes = (UserRenderer,) # email act social media auth app

    # add that only authentication

    def post(self, request):
        # screating profile owner for chess instructor
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data= serializer.validated_data    
  

        # # we check if user is a correct user
        data_user = auth_models.User.objects.get(id=self.request.data['user'])
        request_user = self.request.user 
        if request_user != data_user:
            print("same")
            return response.Response({"error":"wrong user"}, status=status.HTTP_400_BAD_REQUEST)
        
        # we check if user already has a chess instructor account
        if profile_owner_models.Profile_owner.objects.filter(user=self.request.data['user'],profile_type="chess_instructor").exists():
            return response.Response({"error": "instructor exist."})
        serializer.save()
        print(serializer.data)

        # creating chess instructor
        # Chess_Instructor_Profile()

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)