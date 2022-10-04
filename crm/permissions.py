from rest_framework import permissions
from profile_owner.models import Profile_owner 
from .models import Student

# custom permission
class UserIsCoach(permissions.BasePermission):
    message = 'You are not instructor'
    def has_permission(self, request, view):
        try:
            Profile_owner.objects.get(user= request.user,is_instructor=True)
        except:
            return False            

        return True
     

class InstructorIsOwner(permissions.BasePermission):
    message = 'You are not instructor'
    def has_permission(self, request, view):
        try:
            instructor = Profile_owner.objects.get(user= request.user,is_instructor=True)
        except:
            return False            
        student = request.query_params.get('student')
        student_db = Student.objects.get(id=student)

        # print("stuudent_db" , student_db.instructor)
        # print("instructor_db" , instructor)
        if student_db.instructor != instructor :
            return False
        return True