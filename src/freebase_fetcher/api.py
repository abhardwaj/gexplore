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
    'scoring': 'freebase'   
  };
  
  for k, v in params.iteritems():
    search_params[k] = v
  
  url = url + '?' + urllib.urlencode(search_params)
  res = urllib.urlopen(url).read()
  return json.loads(res)



print fetch_url(FREEBASE_URL, {'query': 'vista points near san francisco'})