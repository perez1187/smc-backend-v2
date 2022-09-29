from django.urls import path
from .views import ProfilesAPIView, ProfilesFilteredAPIView, ImageViewSet
 
#profile-owner/
urlpatterns = [
    path('profiles3/', ProfilesAPIView.as_view(), name="my-profiles"),
    path('profiles/', ProfilesFilteredAPIView.as_view(), name="profiles"),
    path('upload/', ImageViewSet.as_view(), name='upload'),

]