class SolarPILOT(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	c_atm_0 = float
	c_atm_1 = float
	c_atm_2 = float
	c_atm_3 = float
	calc_fluxmaps = float
	cant_type = float
	check_max_flux = float
	contingency_rate = float
	cost_sf_fixed = float
	delta_flux_hrs = float
	dens_mirror = float
	dni_des = float
	flux_max = float
	focus_type = float
	h_tower = float
	helio_active_fraction = float
	helio_height = float
	helio_optical_error = float
	helio_positions_in = tuple
	helio_reflectance = float
	helio_width = float
	heliostat_spec_cost = float
	is_optimize = float
	land_max = float
	land_min = float
	land_spec_cost = float
	n_facet_x = float
	n_facet_y = float
	n_flux_days = float
	n_flux_x = float
	n_flux_y = float
	opt_algorithm = float
	opt_conv_tol = float
	opt_flux_penalty = float
	opt_init_step = float
	opt_max_iter = float
	q_design = float
	rec_absorptance = float
	rec_aspect = float
	rec_cost_exp = float
	rec_height = float
	rec_hl_perm2 = float
	rec_ref_area = float
	rec_ref_cost = float
	sales_tax_frac = float
	sales_tax_rate = float
	site_spec_cost = float
	solar_resource_file = str
	tower_exp = float
	tower_fixed_cost = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	area_sf = float
	base_land_area = float
	cost_land_tot = float
	cost_rec_tot = float
	cost_sf_tot = float
	cost_site_tot = float
	cost_tower_tot = float
	flux_max_observed = float
	flux_table = tuple
	h_tower_opt = float
	heliostat_positions = tuple
	land_area = float
	number_heliostats = float
	opteff_table = tuple
	rec_aspect_opt = float
	rec_height_opt = float


class Solarpilot(object):
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

	SolarPILOT = SolarPILOT
	Outputs = Outputs


def default(config) -> Solarpilot
	pass

def new() -> Solarpilot
	pass

def wrap(ssc_data_t) -> Solarpilot
	pass

__loader__ = None 

__spec__ = None
