import csv
import os
import re
#from decimal import *
from defs import freq_cleaner, geo_convert
base_dir = os.getcwd()

def station_cord(name, freq, state):
	if name != None:
		radio_table = open(base_dir+'/radio_list.csv', 'r') #open data from radio list
		radio_reader = csv.DictReader(radio_table) #read data
		for column in radio_reader:
			if re.findall(name,column['Call']) != []:#in call column find all 'name'
				given_freq = int(float(column['Frequency'].replace('MHz','').replace(' ','')))
				
				if freq < given_freq + 1 and freq > given_freq - 1:
					print '--- '+str(freq) + ' matched freq ' + column['Frequency']
					lat = geo_convert(column['lat_deg'], column['lat_min'], column['lat_sec'])
					lng = geo_convert(column['lng_deg'], column['lng_min'],column['lng_sec'])*-1 #negative is west, must be modified if outside US
					freq = freq_cleaner(column['Frequency'])
					return [lat, lng, freq]
	else:
		return [None, None, None]

#later you can add sometihing to match frequency and state...get to table first