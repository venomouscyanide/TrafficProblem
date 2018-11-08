from Classes.vehicle import vehicle
from Classes.weather import weather
from Classes.orbit import orbit
'''
Contains the function that initializes the values according 
to the given problem statement
'''
def initialize(orbit1_speed,orbit2_speed):
	'''
	function to initialize the class instances with values
	as per the problem 
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

	return (weather_names,vehicle_names,vehicles_object_list,
		weathers_object_list,orbits_object_list,priority)
