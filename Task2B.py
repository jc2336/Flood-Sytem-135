
from floodsystem.stationdata import build_station_list, update_water_levels, MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import relative_water_level

def run():
    stations = build_station_list() 
    tol = 0.8
    update_water_levels(stations)

    print(stations_level_over_threshold(stations,tol))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
