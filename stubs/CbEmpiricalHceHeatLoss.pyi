class Hce(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	HCEFrac = tuple
	HCE_A0 = tuple
	HCE_A1 = tuple
	HCE_A2 = tuple
	HCE_A3 = tuple
	HCE_A4 = tuple
	HCE_A5 = tuple
	HCE_A6 = tuple
	PerfFac = tuple
	RefMirrAper = tuple
	SfInTempD = float
	SfOutTempD = float
	ui_reference_ambient_temperature = float
	ui_reference_direct_normal_irradiance = float
	ui_reference_wind_speed = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	HL = tuple
	HL_weighted = float
	HL_weighted_m2 = float


class CbEmpiricalHceHeatLoss(object):
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

	Hce = Hce
	Outputs = Outputs


def default(config) -> CbEmpiricalHceHeatLoss
	pass

def new() -> CbEmpiricalHceHeatLoss
	pass

def wrap(ssc_data_t) -> CbEmpiricalHceHeatLoss
	pass

__loader__ = None 

__spec__ = None
