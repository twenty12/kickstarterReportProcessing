"""
Created on 1/27/14

Script for sorting python data in clean.csv

@author: danielgladstone
"""
import csv
import os
from defs import basic_columns, added_columns, all_cleaned, in_range, out_range, base_dir






clean_table = open(all_cleaned, 'r') #open data from radio list
clean_reader = csv.DictReader(clean_table) #read data

total_d  = 0
total_fspl = 0

total_ents = 0 

#for column in clean_reader:
#	total_d = total_d + int(float(column['distance']))
#	total_fspl = total_fspl + int(float(column['db']))
#	total_ents = total_ents + 1
#	entries= [column['id'],column['name'],column['email'],column['country'],column['min_reward'],column['pledge'],column['status'],column['notes'],column['ship_name'],column['address_1'],column['address_2'],column['city'],column['zip'],column['ship_country'],column['state'],column['station_freq'],column['station_call'],column['cleaned_frequency'],column['cleaned_call'],column['backer_lat'],column['backer_lng'],column['rad_lat'],column['rad_lng'],column['distance'],column['db']]

clean_table = open(all_cleaned) #open data from radio list
clean_reader = csv.DictReader(clean_table) #read data
#av_fspl = total_fspl/total_ents
#cut_off = av_fspl*1.2
cut_off = 100

for column in clean_reader:
	entries= [column['id'],column['name'],column['email'],column['country'],column['min_reward'],column['pledge'],column['status'],column['notes'],column['ship_name'],column['address_1'],column['address_2'],column['city'],column['zip'],column['ship_country'],column['state'],column['station_freq'],column['station_call'],column['cleaned_frequency'],column['cleaned_call'],column['backer_lat'],column['backer_lng'],column['rad_lat'],column['rad_lng'],column['distance'],column['db']]
	
	if int(float(column['distance'])) < cut_off:
		print 'in range: ' + str(column['distance'])
		t_in_range =  open(in_range,'a')
		w_in_range = csv.writer(t_in_range)
		w_in_range.writerow(entries)
		t_in_range.close()
	else:
		print 'out range: ' + str(column['distance'])
		t_out_range =  open(out_range,'a')
		w_out_range = csv.writer(t_out_range)
		w_out_range.writerow(entries)
		t_out_range.close()
clean_table.close()