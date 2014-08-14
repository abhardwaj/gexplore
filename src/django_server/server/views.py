import json

from django.http import *
from django.shortcuts import render_to_response

'''
@author: Anant Bhardwaj
@date: Mar 21, 2013

GExplorer Web Handler
'''

def search(request):
  return render_to_response("search.html")

def place(request):
  p = {}
  if 'place' not in request.REQUEST:
    return HttpResponse("Missing place value in the query")
  
  place = request.REQUEST['place']
  if place.strip() == '':
    return HttpResponse("Empty value for place")
  
  p['place'] = place

  if 'type' in request.REQUEST:
    try:
      p['type'] = int(request.REQUEST['type'])
    except:
      p['type'] = -1
  
  return render_to_response("place.html", p)