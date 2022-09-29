from rest_framework import generics, response, status

import vimeo
from decouple import config


client = vimeo.VimeoClient(
    token= config('token'),
    key= config('key'),
    secret=config('secret')
)


class CreateVideoAPIView(generics.GenericAPIView):

    def post(self, request):
        print("self",self)
        print("request", request.body['filename'])

        return response.Response({"success":"hahaha"}, status=status.HTTP_201_CREATED)