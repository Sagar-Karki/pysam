class WeatherReader(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	file_name = str
	interpolate = float
	requested_ht = float
	scan_header_only = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	city = str
	closest_dir_meas_ht = float
	closest_speed_meas_ht = float
	country = str
	description = str
	elev = float
	lat = float
	location_id = str
	lon = float
	pressure = tuple
	state = str
	temperature = tuple
	wind_direction = tuple
	wind_speed = tuple
	year = float


class WindFileReader(object):
	def assign(self, dict):
		pass

	def execute(self, int_verbosity):
		pass

	def export(self):
		pass

	def __getattribute__(self, *args, **kwargs):
		pass

	def __init__(self, *args, **kwargs):
		pass

	WeatherReader = WeatherReader
	Outputs = Outputs


def default(config) -> WindFileReader
	pass

def new() -> WindFileReader
	pass

def wrap(ssc_data_t) -> WindFileReader
	pass

__loader__ = None 

__spec__ = None
