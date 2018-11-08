from Classes.vehicle import vehicle
from Classes.weather import weather
from Classes.orbit import orbit
'''
Contains the function that initializes the values according 
to the given problem statement inputs
'''
def take_user_input():
	'''
	Help in selecting which problem in Set3
	'''
	selection=int(input("Select 1 for Set3Problem1, 2 for Set3Problem2:"))
	print("Proceed with input",end="\n")
	
	'''
	get the inputted weather
	'''
	weather_inputted=input().split()
	weather_inputted=weather_inputted[2]

	'''
	input the two orbit speeds
	'''
	orbit_speeds=[]

	if(selection==1):
		orbit_number=2#only 2 for Set3Problem1
	elif(selection==2):
		orbit_number=4#4 orbits for Set3Problem2

	for i in range(orbit_number):
		'''
		extract out and store the orbit speeds
		'''
		orb_spd=input().split()
		for j in orb_spd:
			try:
				if(int(j)):
					orbit_speeds.append(int(j))
			except:
				pass
	
	
	return orbit_speeds,weather_inputted,selection

def initialize(orbit_speeds,selection):
	'''
	function to initialize the class instances with values
	as per the problem 
	'''
	orbit1=orbit(1,18,20,orbit_speeds[0])
	orbit2=orbit(2,20,10,orbit_speeds[1])

	if(selection==2):
		orbit3=orbit(3,30,15,orbit_speeds[2])
		orbit4=orbit(4,15,18,orbit_speeds[3])	

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
	destinations=["Hallitharam","RK Puram"]

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

	if(selection==1):
		orbits_object_list.extend([orbit1,orbit2])#only need 2 orbits for Set3Problem1
	elif(selection==2):
		orbits_object_list.extend([orbit1,orbit2,orbit3])#need 3 for Set3Problem2
	
	return (weather_names,vehicle_names,vehicles_object_list,
		weathers_object_list,orbits_object_list,priority,destinations)
