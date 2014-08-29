from django.conf import settings
from django.http import HttpResponse
import os.path
import urllib
import requests
import json


media_dir = settings.MEDIA_ROOT + '/vine-thumbs/'


def cURL (url):
    r = requests.get(url)
    return r.text


def saveImage (url, destination):
    if not imageExists(destination):
        data = cURL(url)
        urllib.urlretrieve(url, media_dir + destination)


def read (url):
    data = cURL(url)

    if data:
        return json.loads(data)


def showImage (filename):
    if imageExists(filename):
        image = open(media_dir + filename, 'rb').read()
        return HttpResponse(image, content_type="image/jpeg")
    else:
        return False


def imageExists (filename):
    return os.path.isfile(media_dir + filename)