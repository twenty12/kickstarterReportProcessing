#example of haversine formulia used to determine distance between to geographic cordinates
#http://www.movable-type.co.uk/scripts/latlong.html

#example of Friis transmission equation to estimate path loss
#http://www.radio-electronics.com/info/propagation/path-loss/free-space-formula-equation.php

#both calcs are done using Graham Galatro's info (he is the first name on the backer list)

import math
from defs import distance_calc

#384 Himrod St Brooklyn NY cordinated from google maps (not the API)
my_lat = math.radians(40.703556)
my_lng =math.radians(-73.916125)
bk_lat =math.radians(40.703556)
bk_lng =math.radians(-73.916125)


rad_lat = math.radians(40.788611)
rad_lng = math.radians(-74.255556)


dlng = (my_lng - rad_lng)*math.pi/180
dlat = (my_lat - rad_lat)*math.pi/180

r = 6371 #rad of eart in km
#print(bk_lat, bk_lng, rad_lat, rad_lng)
d = math.acos( math.sin(bk_lat) * math.sin(rad_lat) + math.cos(bk_lat) * math.cos(rad_lat)* math.cos(rad_lng - bk_lng) ) * r
#print 'Calculater Distance: ' + str(distance_calc(40.788611, -74.255556, 40.703454, -73.916141))
print 'Calculater Distance: ' + str(distance_calc(-96.996631,32.55227,32.588611, -96.968056))
print 'Calculater Distance: ' + str(distance_calc(32.55227,-96.996631, 32.588611, -96.968056))
#print(rad_lat, rad_lng, bk_lat, bk_lng)
#print 'Calculater Distance: ' + str(distance_calc(rad_lat, rad_lng, bk_lat, bk_lng))
#print 'DISTANCE ' + str(d)

f = 91.1

c = 299792.458 #m/s

wl = 299792458/(f*1000000)

fspl = math.pow(((4*math.pi*d*f)/c), 2)