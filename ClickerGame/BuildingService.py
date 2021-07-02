import Building
from dictionary import *


class BuildingService:
    def __init__(self):
        self.speak_to_someone = Building.Building(building_dict1)
        self.megaphone = Building.Building(building_dict2)
        self.internet_ad = Building.Building(building_dict3)
        self.tv_ad = Building.Building(building_dict4)
        self.superbowl_ad = Building.Building(building_dict5)
        self.speak_to_the_world = Building.Building(building_dict6)
        self.solar_system = Building.Building(building_dict7)
        self.galaxy = Building.Building(building_dict8)
        self.universe = Building.Building(building_dict9)
        self.other_dimensions = Building.Building(building_dict10)
        self.building_list = [self.speak_to_someone,
                              self.megaphone,
                              self.internet_ad,
                              self.tv_ad,
                              self.superbowl_ad,
                              self.speak_to_the_world,
                              self.solar_system,
                              self.galaxy,
                              self.universe,
                              self.other_dimensions]
