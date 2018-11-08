class orbit:
	'''
	class orbit with distance and crater no in it
	'''
	def __init__(self,number,distance=0,craters=0,speed=0):
		self.__number=number
		self.__distance=distance
		self.__craters=craters
		self.__list_of_times=[]
		self.__speed=speed

	def get_details(self):
		'''
		simple function to get the orbit class contents
		'''
		return (self.__distance,self.__craters)

	def calculate_speeds(self,vehicles,weather):
		crater_percentage=weather.get_details()#to find the actual number of craters
		self.__craters=self.__craters+(self.__craters*crater_percentage)#increase or decrease no based on weather

		for x in vehicles:#iterate through every vehicle in that orbit
			vehicle_speed,vehicle_crater_time=x.get_details()
			'''
			choose the maximum speed as that of the vehicle 
			or the upper limit in that particular orbit
			'''
			vehicle_speed=self.__speed if self.__speed<vehicle_speed else vehicle_speed
			
			crater_covering_time=vehicle_crater_time*self.__craters#time to cover craters in minutes
			distance_covering_time=(self.__distance/vehicle_speed)*60#time to cover the distance in minutes

			total_time=crater_covering_time+distance_covering_time#total is just simple addition
			self.__list_of_times.append([self.__number,total_time,x.getname()])
	def get_list(self):
		return(self.__list_of_times)

