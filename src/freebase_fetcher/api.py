import json
import urllib

'''
@author: anant bhardwaj
@date: Oct 4, 2012

API wrappers
''' 

FREEBASE_URL = 'https://www.googleapis.com/freebase/v1/search'

def fetch_url(url, params):  
  url = url + '?' + urllib.urlencode(params)
  res = urllib.urlopen(url).read()
  return json.loads(res)


search_params = {
  'filter': '(all type:/travel/travel_destination part_of:california)'
}
print fetch_url(FREEBASE_URL, search_params)

search_params = {
  'filter': '(all type:restaurant/ part_of:"san francisco")'
}
print fetch_url(FREEBASE_URL, search_params)