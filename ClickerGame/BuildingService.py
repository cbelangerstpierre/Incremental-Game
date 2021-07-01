import building
from dictionary import *


class BuildingService:
    def __init__(self):
        self.speak_to_someone = building.Building(building_dict1)
        self.megaphone = building.Building(building_dict2)
        self.internet_ad = building.Building(building_dict3)
        self.tv_ad = building.Building(building_dict4)
        self.superbowl_ad = building.Building(building_dict5)
        self.speak_to_the_world = building.Building(building_dict6)
        self.solar_system = building.Building(building_dict7)
        self.galaxy = building.Building(building_dict8)
        self.universe = building.Building(building_dict9)
        self.other_dimensions = building.Building(building_dict10)
        self.building_list = [self.speak_to_the_world,
                              self.megaphone,
                              self.internet_ad,
                              self.tv_ad,
                              self.superbowl_ad,
                              self.speak_to_the_world,
                              self.solar_system,
                              self.galaxy,
                              self.universe,
                              self.other_dimensions]
