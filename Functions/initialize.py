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

def hardcoded_values():
	'''
	This function is the only place of hard 
	coding the values as needed. 
	'''
	weather1=weather(-.1,"Sunny")
	weather2=weather(.2,"Rainy")
	weather3=weather(0,"Windy")

	vehicle1=vehicle(10,2,"Bike")
	vehicle2=vehicle(12,1,"TukTuk")
	vehicle3=vehicle(20,3,"Car")

	destinations=["Hallitharam","RK Puram"]#as per problem. Hardcoded

	weather1.vehicles_allowed(vehicle1.getname())
	weather1.vehicles_allowed(vehicle2.getname())
	weather1.vehicles_allowed(vehicle3.getname())

	weather2.vehicles_allowed(vehicle2.getname())
	weather2.vehicles_allowed(vehicle3.getname())

	weather3.vehicles_allowed(vehicle1.getname())
	weather3.vehicles_allowed(vehicle3.getname())

	return weather1,weather2,weather3, \
			vehicle1,vehicle2,vehicle3,destinations

def initialize_objects_helper():
	'''
	Helps initialize the class instances with
	hardcoded values for vehicles and weather
	'''
	weather1,weather2,weather3, \
	vehicle1,vehicle2,vehicle3,destinations=hardcoded_values()

	'''
	get the list of weather,vehicle names
	'''
	weather_names=[]
	weather_names.extend([weather1.getname(),weather2.getname(),weather3.getname()])

	vehicle_names=[]
	vehicle_names.extend([vehicle1.getname(),vehicle2.getname(),vehicle3.getname()])

	'''
	get the list of vehicle,weather,orbit objects
	'''
	vehicles_object_list=[]
	vehicles_object_list.extend([vehicle1,vehicle2,vehicle3])

	weathers_object_list=[]
	weathers_object_list.extend([weather1,weather2,weather3])


	return(weather_names,vehicle_names,vehicles_object_list,
		weathers_object_list,destinations)

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

	weather_names,vehicle_names,vehicles_object_list, \
		weathers_object_list,destinations=initialize_objects_helper()

	priority=[]
	for i in vehicle_names:
		priority.append(i)#priority bike>tuktuk>car
	
	orbits_object_list=[]

	if(selection==1):
		orbits_object_list.extend([orbit1,orbit2])#only need 2 orbits for Set3Problem1
	elif(selection==2):
		orbits_object_list.extend([orbit1,orbit2,orbit3])#need 3 for Set3Problem2
	
	return (weather_names,vehicle_names,vehicles_object_list,
		weathers_object_list,orbits_object_list,priority,destinations)
