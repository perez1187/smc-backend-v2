from django.urls import path
from .views import ProfilesAPIView, ProfilesFilteredAPIView, ImageViewSet, ProfileAPIVIew,ProfileUpdateAPIView, CreateProfileOwnerApiView
 
#profile-owner/
urlpatterns = [
    path('create/', CreateProfileOwnerApiView.as_view(), name="createProfiles"),
    path('profiles3/', ProfilesAPIView.as_view(), name="my-profiles"),
    path('profiles/', ProfilesFilteredAPIView.as_view(), name="profiles"),
    path('upload/', ImageViewSet.as_view(), name='upload'),
    path('profiles/<int:id>', ProfileAPIVIew.as_view(), name="profile"),
    path('profiles/update/<int:id>', ProfileUpdateAPIView.as_view(), name="profiles"),

]