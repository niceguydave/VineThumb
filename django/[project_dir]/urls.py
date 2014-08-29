from django.conf.urls import patterns, include, url
from django.conf import settings
from django.http import HttpResponse

urlpatterns = patterns('',
    (r'^vine-thumb/[a-zA-Z0-9]{10,15}', include('vinethumbs.urls', namespace="vinethumb"))
)