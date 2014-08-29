from django.conf.urls import patterns, url
from vinethumbs import views

urlpatterns = patterns('',
    url(r'^$', views.VineThumbnail, name="vine-thumbnail"),
)