from api.celery import app
from .models import UploadVideo
import vimeo
from decouple import config

client = vimeo.VimeoClient(
    token= config('token'),
    key= config('key'),
    secret=config('secret')
)



@app.task(bind=True)
def upload_video(self, video_id, link_lokal_my):
    #pass

    video = UploadVideo.objects.get(id=video_id)
    video.status="chujs"

    print(self)
    #print("link lokal", link_lokal)

    file_name = link_lokal_my
    uri = client.upload(file_name, data={
      'name': 'test3',
      'description': 'The description goes here.'
    })
    print('Your video URI is: %s' % (uri))
    print(uri)
    video.link_lokal = uri

    video.save()