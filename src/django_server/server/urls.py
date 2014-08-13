from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^$', 'server.views.freebase_suggest'),
  url(r'freebase$', 'server.views.freebase_suggest'),
  url(r'maps$', 'server.views.maps_suggest'),
    )
