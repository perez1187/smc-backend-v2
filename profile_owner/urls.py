from django.urls import path
from .views import MyProfilesAPIView
 
#profile-owner/
urlpatterns = [
    path('my-profiles/', MyProfilesAPIView.as_view(), name="my-profiles"),

]