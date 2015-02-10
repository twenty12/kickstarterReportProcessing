"""
Created on 1/27/14

This script uses functions in def.py to process backer information. After processing data goes into one of three files:
	-international.csv (backers with 'Shipping Country Name' not US)
	-problem.csv (backrs with call numbers not in FM list)
	-all_cleaned.cvs (backers who station was found on backer list)

all_cleaned includes all the relivent data for sorting:
	-backers lat/long
	-cleaned station call letters
	-stations lat/long

@author: danielgladstone
"""

import time
import csv
import re
import os
from defs import call_cleaner, freq_cleaner, distance_calc, fspl_calc, in_system, geo
from defs import basic_columns, added_columns, inter, problem, all_cleaned, station, input_call_letters, files, base_dir
from table_search import station_cord #this function needs to be imported seperately, not sure why. 
from geolocation.google_maps import GoogleMaps


i=1
for report in files:
	if report == '.DS_Store':
		continue
	with open(base_dir+'/backer_reports(raw)/'+report,'r') as csvfile:
		reader = csv.DictReader(csvfile)	#opens as a dictionary keyed by column names
		for column in reader:
			print ''
			print ''
			print 'Loop number: ' + str(i)
			print '- Current backer: ' + column['Backer Id']
			if in_system(column['Backer Id']) == False:
				
				print '-- Adding backer: '+column['Backer Id']
				
				basic_entries = [column['Backer Id'], column['Backer Name'], column['Email'], column['Shipping Country'], column['Shipping Amount'], column['Pledge Amount'], column['Pledged Status'], column['Notes'], column['Shipping Name'], column['Shipping Address 1'], column['Shipping Address 2'], column['Shipping City'], column['Shipping State'], column['Shipping Postal Code'], column['Shipping Country Name'], column[station], column[input_call_letters]]
				
				if column['Shipping Country Name'] == 'United States':
					freq = freq_cleaner(column[station])
					call_letters = call_cleaner(column[input_call_letters])
					rad_cord = station_cord(call_letters, freq, column['Shipping City'])
					address = column['Shipping Address 1']
					city = column['Shipping City']
					zipcode = column['Shipping Postal Code']
					state = column['Shipping State']
				
				else:#international entries
					t_inter =  open(inter,'a')
					f = csv.writer(t_inter)
					f.writerow(basic_entries)
					t_inter.close()
					print '--- Added International backer: '+column['Backer Id']
					print '---- Done with backer : '+column['Backer Id']
					i = i-1
					if i==0:
						break
					continue #continues to next loop
				
				if freq != None and rad_cord != None and rad_cord[0] != None:
					print '--' + (address + ' ' + city + ' ' + state)
					
					bk_cord = geo(address, city, state, zipcode)
					if bk_cord == 'skip':
						continue
					distance = distance_calc(rad_cord[0], rad_cord[1], bk_cord.lat, bk_cord.lng)
					fspl = fspl_calc(distance, rad_cord[2]) #rad_cord[2] is station frequency
					add_entries = [freq, call_letters, bk_cord.lat, bk_cord.lng, rad_cord[0], rad_cord[1], distance, fspl]
					
					t_all_cleaned =  open(all_cleaned,'a')
					f = csv.writer(t_all_cleaned)
					f.writerow(basic_entries + add_entries)
					t_all_cleaned.close()
					bk_cord.lat = None
					bk_cord.lng = None
					rad_cord = None
					print '--- Added clean backer: '+column['Backer Id']
				
				else: #problem entries
					t_problem =  open(problem,'a')
					f = csv.writer(t_problem)
					f.writerow(basic_entries)
					t_problem.close()
					rad_cord = None
					print '--- Added Problem backer: '+column['Backer Id']
			else:
				print '-- Backer in system: '+column['Backer Id']
				
			print '-- Done with backer : '+column['Backer Id']
			i = i-1
			#if i==0:
			#	break