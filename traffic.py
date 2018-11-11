#Set3Problem1 and Set3Problem2
#Revision V2.1. See changelist
from Classes.vehicle import vehicle
from Classes.weather import weather
from Classes.orbit import orbit
from Functions.logic import print_the_fastest
from Functions.logic import fastest_vehicle
from Functions.logic import decide_route
from Functions.initialize import initialize
from Functions.initialize import take_user_input


if __name__ == '__main__':
	'''
	the driver function to print the fastest vehicle 
	'''

	'''
	function to take input from STDIN
	'''
	orbit_speeds,weather_inputted,selection=take_user_input()

	'''
	set all the values of the classes as per requirement using
	initialize()
	'''
	weather_names,vehicle_names,vehicles_object_list, \
	weathers_object_list,orbits_object_list,priority,destinations=initialize(orbit_speeds,selection)
	
	'''
	finding the index of the weather to know
	which weather object to use
	'''
	for i in weather_names:
		if(i==weather_inputted):
			weather_index=weather_names.index(i)
			break
	
	'''
	find out the vehicles allowed in the inputted weather
	'''

	vehicles_allowed=weathers_object_list[weather_index].get_allowed_vehicles()

	vehicles_allowed_objects=[]
	'''
	get a list of all the allowed vehicle's objects in the particular weather
	from the vehicle objects list
	'''
	for x in vehicles_allowed:	
		vehicles_allowed_objects.append(vehicles_object_list[vehicle_names.index(x)])

	'''
	pass the orbit objects,orbit1 speed, orbit2 speed, allowed vehicles' object list,
	weather object of inputted weather
 	'''
	fastest_vehicle,fastest_orbit=fastest_vehicle(orbits_object_list,
			vehicles_allowed_objects,weathers_object_list[weather_index],
			priority)
	
	'''
	finally print the fastest vehicle in which orbit number and the route if necessary
	'''
	if(selection==1):
		print("Vehicle {vehicle} on Orbit{orbit_no}".format(vehicle=fastest_vehicle,orbit_no=fastest_orbit))

	elif(selection==2):
		destinations_ordered,orbit2=decide_route(fastest_orbit,fastest_vehicle,destinations)
		
		print("Vehicle {vehicle} to {dest1} via Orbit{orbit_no1} and {dest2} via Orbit{orbit_no2}".
			format(vehicle=fastest_vehicle,dest1=destinations_ordered[0],orbit_no1=fastest_orbit,
				dest2=destinations_ordered[1],orbit_no2=orbit2))

	