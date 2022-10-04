from rest_framework import generics, permissions, views,response, status
from .models import Student
from .serializers import StudentListSerializer
from profile_owner.models import Profile_owner
from authentication import authentication
from .permissions import UserIsCoach

class StudentListAPIView(generics.ListAPIView):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes = (UserIsCoach,)

    def get_queryset(self):
        user = self.request.user # that give us email from token 
        profile_owner = Profile_owner.objects.get(user= user.id,is_instructor=True)
        
        return Student.objects.filter(instructor=profile_owner.id) # is owner of user account

class AddStudent(generics.CreateAPIView):
    serializer_class = StudentListSerializer
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes = (UserIsCoach,)

class RetriveupdateDestroyStudentAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()
    lookup_field = "id"
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes=(UserIsCoach,)