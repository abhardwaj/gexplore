import json

from django.http import *
from django.shortcuts import render_to_response

'''
@author: Anant Bhardwaj
@date: Mar 21, 2013

GExplorer Web Handler
'''

def freebase_suggest(request):
  return render_to_response("freebase_suggest.html")

def maps_suggest(request):
  return render_to_response("maps_suggest.html")

def maps_suggest_google(request):
  return render_to_response("maps_suggest_google.html")