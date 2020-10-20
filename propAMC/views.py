from .forms import *
from .models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework import compat
from django.views import View
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
from django.contrib import messages
import json
import openpyxl
import pandas as pd
import requests


def findGeocode(city):
	from geopy.geocoders import Nominatim
	try:
		geolocator = Nominatim(user_agent="propApp")
		return geolocator.geocode(city)
	except GeocoderTimedOut:
		return findGeocode(city)

def index(request):
    form = UserForm(request.POST,request.FILES)
    template = "index.html"
    data = UserFile.objects.all().values()
	# context = {}
    context = {"form": form,"object_list" : data}
    if form.is_valid():
    	fileName = request.POST.get("file_name")
    	file_name = 'media/files/'+fileName
    	# print(type(fileName))
    	obj = form.save(commit=False)
    	obj.save()
    	addressToLatLong(file_name)
    	return HttpResponseRedirect("/")
    else: 
        form = UserForm()   
    return render(request, template, context)

def addressToLatLong(file_name):
	df = pd.read_excel(file_name)
	Citylist=[]
	Latlist=[]
	Longlist=[]
	for i in df.index:
	    data=df['address'][i]
	    Citylist.append(data)
	    loc = findGeocode(data)
	    loca1 = loc.latitude
	    loca2 = loc.longitude
	    Latlist.append(loca1)
	    Longlist.append(loca2)

	df=pd.DataFrame({'address':Citylist,'latitude':Latlist,'longitude':Longlist})
	df.to_excel(file_name,index=False)
	# print(pd.read_excel(file_name))


def funGeoCodeApi():
	api_key = 'AIzaSyBbIzRABXYrhKMTfKy2Tfl5EDGN6'
	url = 'https://maps.googleapis.com/maps/api/geocode/json?'
	place = 'Bareilly' 
	requestData = requests.get(url + 'address =' +place + '&key =' + api_key) 
	x = requestData.json() 
	print(x) 




