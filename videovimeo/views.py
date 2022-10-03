from rest_framework import generics, response, status
from .serializers import VideoSerializer

import vimeo
from decouple import config

from api.celery import app
from .tasks import upload_video

from authentication import authentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


client = vimeo.VimeoClient(
    token= config('token'),
    key= config('key'),
    secret=config('secret')
)


class CreateVideoAPIView(generics.GenericAPIView):

    serializer_class = VideoSerializer
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes=(IsAuthenticatedOrReadOnly,)
  
    def post(self, request):
       
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True) 
        data = serializer._validated_data
        serializer.save()
        
        # upload video vimeo celery + redis
        #upload_video.delay(serializer.data['id'],data["link"])        


        return response.Response({"success":"hahaha","video:":"uri"}, status=status.HTTP_201_CREATED)