from django.urls import path
from .views import StudentListAPIView, AddStudent, RetriveupdateDestroyStudentAPIView
 
#crm/
urlpatterns = [
    path('student_list/', StudentListAPIView.as_view(), name="student_list"),
    path('add/', AddStudent.as_view(), name="add"),
    path('student_list/<int:id>/', RetriveupdateDestroyStudentAPIView.as_view(), name="student_list-id"),
]

