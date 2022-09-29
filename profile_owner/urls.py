from django.urls import path
from .views import MyProfilesAPIView, ProfilesFilteredAPIView
 
#profile-owner/
urlpatterns = [
    path('my-profiles/', MyProfilesAPIView.as_view(), name="my-profiles"),
    path('profiles/', ProfilesFilteredAPIView.as_view(), name="profiles"),

]