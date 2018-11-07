class weather:
	'''
	class weather with crater crater_percentage(increase or decrease)
	and name of the weather
	'''
	def __init__(self,crater_percentage=0,name=""):
		self.__crater_percentage=crater_percentage
		self.__name=name
		self.__vehicles_allowed=[]

	def getname(self):
		return self.__name

	def get_details(self):
		return(self.__crater_percentage)

	def vehicles_allowed(self,vehicle):
		'''
		append each vehicle allowed in the particular weather
		'''
		self.__vehicles_allowed.append(vehicle)

	def get_allowed_vehicles(self):
		'''
		returns the list of all allowed vehicles for the 
		particular weather
		'''
		return self.__vehicles_allowed
