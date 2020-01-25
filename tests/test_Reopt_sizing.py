import pytest
from pympler.tracker import SummaryTracker
import gc
import PySAM.Pvwattsv7 as pv
import PySAM.Battwatts as bt
import PySAM.Utilityrate5 as ur
import PySAM.Pvsamv1 as pvsam
import PySAM.StandAloneBattery as stbt


def test_reopt_sizing_pvwatts():
    round = 0

    tracker = SummaryTracker()
    while round < 55:   # multiple runs required to check for memory leaks
        round += 1

        sys = pv.default("PVWattsCommercial")
        sys.SolarResource.solar_resource_file = "/Users/dguittet/SAM-Dev/sam/deploy/solar_resource/blythe_ca_33.617773_-114.588261_psmv3_60_tmy.csv"
        batt = bt.from_existing(sys, "PVWattsCommercial")
        sys.SolarResource.solar_resource_data = dict({'lat': 3, 'lon': 3})
        batt.Battery.crit_load = [0] * 8760
        fin = ur.from_existing(sys, "PVWattsCommercial")

        post = sys.Reopt_size_battery_post()

    assert('Scenario' in post['reopt_post'])
    tracker_diff = tracker.diff()
    for i in range(len(tracker_diff)):
        if len(tracker_diff[i]) > 1:
            assert(tracker_diff[i][1] < 10)
    assert(post['reopt_post']['Scenario']['Site']['latitude'] == pytest.approx(3, 0.1))


def test_reopt_sizing_pvsam():
    import PySAM.Utilityrate5 as ur
    sys = pvsam.default("FlatPlatePVCommercial")
    fin = ur.from_existing(sys, "FlatPlatePVCommercial")
    bt = stbt.from_existing(sys, "BatteryNone")

    sys.SolarResource.solar_resource_file = "/Users/dguittet/SAM-Dev/sam/deploy/solar_resource/blythe_ca_33.617773_-114.588261_psmv3_60_tmy.csv"
    bt.Load.crit_load = [0] * 8760
    post = sys.Reopt_size_battery_post()

    assert('Scenario' in post['reopt_post'])
    assert(post['reopt_post']['Scenario']['Site']['latitude'] == pytest.approx(33.6, 0.1))

