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
# other aps
from profile_owner import models as profile_owner_models

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

    def post(self, request):
        # save user to db
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)