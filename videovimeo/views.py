from rest_framework import generics, response, status
from .serializers import VideoSerializer

import vimeo
from decouple import config


client = vimeo.VimeoClient(
    token= config('token'),
    key= config('key'),
    secret=config('secret')
)


class CreateVideoAPIView(generics.GenericAPIView):

    serializer_class = VideoSerializer
    def post(self, request):
        print("self",self)
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True) 
        data = serializer._validated_data
        print(data["link_lokal"]) 
       
       
        
        #file_name = './testvideos/P6181178.AVI'
        file_name = data["link_lokal"]
        uri = client.upload(file_name, data={
          'name': 'test3',
          'description': 'The description goes here.'
        })
        print('Your video URI is: %s' % (uri))
        print(uri)

        return response.Response({"success":"hahaha","video:":uri}, status=status.HTTP_201_CREATED)