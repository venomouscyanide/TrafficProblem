#Set3Problem1
#Revision V2.0

from Classes.vehicle import vehicle
from Classes.weather import weather
from Classes.orbit import orbit
from Functions.functions import print_the_fastest
from Functions.functions import fastest_vehicle


if __name__ == '__main__':
	'''
	the driver function to print the fastest vehicle 
	Input: the weather and the max speed in each orbit1_speed
	Output: the fastest vehicle and in which orbit number
	'''

	'''
	get the inputted weather
	'''
	weather_inputted=input().split()
	weather_inputted=weather_inputted[2]

	'''
	input the two orbit speeds
	'''
	inp1=input().split()
	inp2=input().split()
	orbit1_speed=int(inp1[4])
	orbit2_speed=int(inp2[4])
	'''
	set all the values of the classes as per requirement
	'''
	orbit1=orbit(1,18,20,orbit1_speed)
	orbit2=orbit(2,20,10,orbit2_speed)	

	sunny=weather(-.1,"Sunny")
	rainy=weather(.2,"Rainy")
	windy=weather(0,"Windy")

	bike=vehicle(10,2,"Bike")
	tuktuk=vehicle(12,1,"TukTuk")
	car=vehicle(20,3,"Car")

	sunny.vehicles_allowed("Bike")
	sunny.vehicles_allowed("TukTuk")
	sunny.vehicles_allowed("Car")

	rainy.vehicles_allowed("TukTuk")
	rainy.vehicles_allowed("Car")

	windy.vehicles_allowed("Bike")
	windy.vehicles_allowed("Car")

	priority=["Bike","TukTuk","Car"]

	'''
	get the list of weather,vehicle names
	'''
	weather_names=[]
	weather_names.extend([sunny.getname(),rainy.getname(),windy.getname()])

	vehicle_names=[]
	vehicle_names.extend([bike.getname(),tuktuk.getname(),car.getname()])

	'''
	get the list of vehicle,weather,orbit objects
	'''
	vehicles_object_list=[]
	vehicles_object_list.extend([bike,tuktuk,car])

	weathers_object_list=[]
	weathers_object_list.extend([sunny,rainy,windy])

	orbits_object_list=[]
	orbits_object_list.extend([orbit1,orbit2])

	
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
			vehicles_allowed_objects,weathers_object_list[weather_index],priority)
	
	'''
	finally print the fastest vehicle in which orbit number
	'''
	print("Vehicle {vehicle} on Orbit{orbit_no}".format(vehicle=fastest_vehicle,orbit_no=fastest_orbit))