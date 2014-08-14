from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  	url(r'^$', 'server.views.search'),
  	url(r'^p/(\w+)', 'server.views.place'),
  )
