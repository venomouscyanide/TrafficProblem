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

def fastest_vehicle_helper(orbits,orbit_speed,vehicles,crater_percentage):
	orbit_number=0
	list_of_times=[]

	for x in orbits:#iterate through the two orbits
		distance,craters=x.get_details()
		craters=craters+(craters*crater_percentage)#increase or decrease no based on weather
		
		orbit_speed_popped=orbit_speed.pop(-1)
		orbit_number+=1#can be 1 or 0 

		for y in vehicles:#iterate through every vehicle in that orbit
			vehicle_speed,vehicle_crater_time=y.get_details()
			'''
			choose the maximum speed as that of the vehicle 
			or the upper limit in that particular orbit
			'''
			vehicle_speed=orbit_speed_popped if orbit_speed_popped<vehicle_speed else vehicle_speed
			
			crater_covering_time=vehicle_crater_time*craters#time to cover craters in minutes
			distance_covering_time=(distance/vehicle_speed)*60#time to cover the distance in minutes

			total_time=crater_covering_time+distance_covering_time#total is just simple addition

			list_of_times.append([orbit_number,total_time,y.getname()])#make a list out of all
	return list_of_times

def fastest_vehicle(orbits,orbit1_speed,orbit2_speed,vehicles,weather,priority):
	'''
	the main piece of code where the logic to find the time 
	taken by each vehicle is written. The timing of each vehicle 
	is then stored onto a list,sorted and passed to print_the_fastest() to
	resolve disputes in case of same min_time of more than one vehicle.
	'''
	orbit_speed=[]
	orbit_speed.extend([orbit1_speed,orbit2_speed])
	orbit_speed=orbit_speed[::-1]#to get in order of inputted values

	crater_percentage=weather.get_details()#to find the actual number of craters

	list_of_times=fastest_vehicle_helper(orbits,orbit_speed,vehicles,crater_percentage)

	list_of_times=sorted(list_of_times,key= lambda x:x[1])#sort in ascending order of times
	fastest_orbit=list_of_times[0][0]#get orbit no of the fastest vehicle

	fastest_vehicle=print_the_fastest(list_of_times,priority)#send to function to resolve disputes if any
	return(fastest_vehicle,fastest_orbit)#return to main the fastest vehicle and the orbit number 
