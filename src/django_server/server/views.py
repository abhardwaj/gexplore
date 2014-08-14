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

def place(request, place):
  p = {'place': place}
  return render_to_response("place.html", p)