# -*- coding: utf-8 -*-
"""
Defintions for 

@author: danielgladstone
"""
import ast
from string import digits
#from defs import freq_cleaner, geo_convert
import re
import csv
import os
import math
import time
import random
from geolocation.google_maps import GoogleMaps
from omgeo import Geocoder
google_maps = GoogleMaps(api_key='AIzaSyDevSd4Tb2ZZtl9bZqUhqViAdhQXVHV23k')

base_dir = os.getcwd()
dic = {'[':'', ']':'', "'":'', '"':'', ')':'', '(':'', ' - ':'-'}

class cord:

	kind = 'location'         # class variable shared by all instances

	def __init__(self, lat, lng):
		self.lat = lat 
		self.lng = lng 

#makes API queries at random time incriments. Google API is not always responsive
def geo(address, city, state, zipcode):
	bk_cord = cord(None, None)
	g = Geocoder()
	result = g.geocode(address + ' ' + city + ' ' + state)
	
	#time.sleep(random.randint(6, 10))
	
	if 'PO BOX' in address.upper():
		address = ''
	n = 0 
	while bk_cord.lat == None:
		
		
		#time.sleep(random.randint(6, 10))
		
		if bk_cord.lat == None:
			try:
				print 'cat'
				g = Geocoder()
				result = g.geocode(address + ' ' + city + ' ' + state)
				if len(result)>0: #for blank reults (often for PO Box )
					lng = [c.__dict__ for c in result["candidates"]][0]['x']
					lat =[c.__dict__ for c in result["candidates"]][0]['y']
					bk_cord = cord(lat, lng)
					time.sleep(random.randint(6, 10))
			except IndexError:
				print 'broke cat'
				pass
		try:
			if bk_cord.lat == None:
				k_cord = google_maps.query(location= state + ' ' + city.title() + ' ' + address + ' ' + zipcode ).first()
				time.sleep(random.randint(6, 10))
		
			if bk_cord.lat == None:
				bk_cord = google_maps.query(location=address + ' ' + city + ' ' + state).first()
				time.sleep(random.randint(6, 10))
		except TypeError:
			print '---- Google TypeError'
			time.sleep(random.randint(5, 6))
			pass
		n = n+1
		if n>10:
			print 'break'
			bk_cord = 'skip'
			break
	return bk_cord

#checks if already in table
def in_system(backer_id):
	base_dir = os.getcwd()
	reports = os.listdir(base_dir + '/reports/')
	test = False
	for report in reports: #for all the reports in the directory
		if report != '.DS_Store':
			#print report
			with file(base_dir+'/reports/'+report, 'r') as report_table: #open data from radio list
				report_reader = csv.DictReader(report_table) #read data
				#print type(report_table)
				#print type(report_reader)
				for column in report_reader:
					if column['id'] == backer_id:
						test = True
	return test

#makes replacing things easy
def replace_all(t, dic):
    for i in range(3):
        for i, j in dic.iteritems():
            t = t.replace(i, j)
    return t

#cleans backer's call letters input
def call_cleaner(letters):
	if letters.upper() != 'N/A':
		if letters.isalpha(): #if letters has no digits
			pass
		else: #letters has digits
			letters = letters.translate(None, digits).replace(" ","")
			letters =  replace_all(letters, dic)#removes digitis
		return(letters.upper()[0:7])
	else:
		return(None)

#cleans backer's freqency input
def freq_cleaner(digits):
	try:
		digits = re.findall('\d+\.\d+',digits)[0]
		digits = int(float(digits))
	except (IndexError, TypeError):
		digits = None
		pass
	return(digits)

#converts time cordinates into decimal
def geo_convert(degrees, minutes, seconds):
	try:
		geo = round(float(degrees) + float(minutes)/60 + float(seconds)/3600, 6)
	except ValueError:
		return(None)
	return geo

#estimates distance between radio geo cordinates and backers. See example_calc.py for more info.
def distance_calc(_bk_lat, _bk_lng, _rad_lat, _rad_lng):
	print (_bk_lat, _bk_lng, _rad_lat, _rad_lng)
	bk_lat = math.radians(_bk_lat)
	bk_lng = math.radians(_bk_lng)
	rad_lat = math.radians(_rad_lat)
	rad_lng = math.radians(_rad_lng)
	d = math.acos( math.sin(bk_lat) * math.sin(rad_lat) + math.cos(bk_lat) * math.cos(rad_lat)* math.cos(rad_lng - bk_lng) ) * 6371
	return d

#estimates signal strength. see example_calc.py for more info.
def fspl_calc(distance, freq):
	c = 299792.458
	fspl = math.pow(((4*math.pi*distance*freq)/c), 2)
	return fspl
	

basic_columns = ['id', 'name', 'email', 'country', 'min_reward', 'pledge', 'status', 'notes', 'ship_name', 'address_1', 'address_2', 'city', 'zip', 'ship_country', 'state', 'station_freq', 'station_call']
added_columns = ['cleaned_frequency', 'cleaned_call', 'backer_lat', 'backer_lng', 'rad_lat', 'rad_lng', 'distance', 'db']

inter = base_dir + '/reports/international.csv'
problem = base_dir + '/reports/problem.csv'
all_cleaned = base_dir + '/reports/all_cleaned.csv'
in_range = base_dir + '/reports/in_range.csv'
out_range = base_dir + '/reports/out_range.csv'

station = 'What Fm Frequency Do You Want Your Radio Tuned To? For Example: 92.9 88.3 100.3'
input_call_letters = '''What Are The Call Letters For Your Station? For Example: Wnyc, Kut, Whyy. If You Don't Know, Or Your Station Doesn't Have Any, You Can Write "N/A."'''

files = os.listdir(base_dir + '/backer_reports(raw)/')
