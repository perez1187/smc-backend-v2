from rest_framework import generics, permissions, views,response, status
from .models import Student, Students_note
from .serializers import StudentListSerializer, StudentNotesSerializer
from profile_owner.models import Profile_owner
from authentication import authentication
from .permissions import UserIsCoach, InstructorIsOwner

class StudentListAPIView(generics.ListAPIView):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes = (UserIsCoach,)

    # we show only instructor students
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

class StudentNotesAPIView(generics.ListAPIView):
    serializer_class = StudentNotesSerializer
    queryset = Students_note.objects.all()
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes = (UserIsCoach,InstructorIsOwner)
    
    # instructorIsOnwer - is instructor is student owner

    # we show only instructor students
    # example http://127.0.0.1:8000/crm/student_notes/?student=1
    def get_queryset(self):
        queryset = Students_note.objects.all()
        student = self.request.query_params.get('student')
        if student is not None:        
            queryset=queryset.filter(student=student)
        
        return queryset #Students_note.objects.filter(student=1) # is owner of user account