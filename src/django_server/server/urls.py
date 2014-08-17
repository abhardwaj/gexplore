from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  	url(r'^$', 'server.views.place'),
  	url(r'^p', 'server.views.place'),
  )
