from django.urls import path
from .views import ChessInstructorAPIVIew, CreateChessInstructorAPIView
 
#profiles/
urlpatterns = [
    path('my-chess-instructor/<int:id>/', ChessInstructorAPIVIew.as_view(), name="my-chess-instructor"),
    path('create-chess-instructor/', CreateChessInstructorAPIView.as_view(), name="create-chess-instructor"),

]