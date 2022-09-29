from django.urls import path
from .views import ProfilesAPIView, ProfilesFilteredAPIView
 
#profile-owner/
urlpatterns = [
    path('profiles3/', ProfilesAPIView.as_view(), name="my-profiles"),
    path('profiles/', ProfilesFilteredAPIView.as_view(), name="profiles"),

]