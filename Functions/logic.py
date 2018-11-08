def print_the_fastest(list_of_times,priority):
	'''
	function to get the fastest vehicle and return based
	on priority chosen in case of many vehicles with same fastest time
	'''
	min_time=list_of_times[0][1]

	'''
	create a set of fastest vehicles
	'''
	vehicle_fastest=set()
	for i in list_of_times:
		if(i[1]==min_time):
			vehicle_fastest.add(i[2])

	'''
	the logic to get the fastest vehicle in case there
	are more than one vehicle with the same min_time
	the priority chosen is as follows
	bike>tuktuk>car
	'''
	sorted_vehicles=[]
	for i in range(len(priority)):
		if(priority[i] in vehicle_fastest):
			sorted_vehicles.append(priority[i])	
	
	'''
	return the vehicle with the most priority as mentioned above
	'''
	return(sorted_vehicles[0])


def fastest_vehicle(orbits,vehicles,weather,priority):
	'''
	the main piece of code where the logic to find the time 
	taken by each vehicle is written. The timing of each vehicle 
	is then stored onto a list,sorted and passed to print_the_fastest() to
	resolve disputes in case of same min_time of more than one vehicle.
	'''
	list_of_times=[]
	
	for x in orbits:#iterate through the orbits
		x.calculate_speeds(vehicles,weather)

	for x in orbits:
		list_of_times+=(x.get_list())

	list_of_times=sorted(list_of_times,key= lambda x:x[1])#sort in ascending order of times

	fastest_orbit=list_of_times[0][0]#get orbit no of the fastest vehicle

	fastest_vehicle=print_the_fastest(list_of_times,priority)#send to function to resolve disputes if any
	return(fastest_vehicle,fastest_orbit)#return to main the fastest vehicle and the orbit number 

def decide_route(fastest_orbit,fastest_vehicle,destinations):
	'''
	A simple function to calculate dest1 and dest2
	and which orbit to choose first and which to choose 
	second. The second choice for an orbit will always be 
	orbit4
	'''
	orbit_list1=[1,2]

	if(fastest_orbit in orbit_list1):
		orbit2=4
	else:
		destinations=destinations[::-1]
		orbit2=4

	return(destinations,orbit2)
