from django.urls import path
from . views import CreateVideoAPIView

urlpatterns = [
    path('create/', CreateVideoAPIView.as_view(), name="my-profiles"),
]