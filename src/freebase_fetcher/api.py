import json
import urllib

'''
@author: anant bhardwaj
@date: Oct 4, 2012

API wrappers
''' 

FREEBASE_URL = 'https://www.googleapis.com/freebase/v1/search'

def fetch_url(url, params):
  search_params = {
    'filter': '(all type:/location/)',
    'spell': 'always',
    'scoring': 'freebase',
    'stemmed': True,
   
  };
  
  for k, v in params.iteritems():
    search_params[k] = v
  
  url = url + '?' + urllib.urlencode(search_params)
  res = urllib.urlopen(url).read()
  return json.loads(res)



print fetch_url(FREEBASE_URL, {'query': 'fremont'})