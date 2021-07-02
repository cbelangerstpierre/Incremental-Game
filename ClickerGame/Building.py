class Building:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.level = dictionary["level"]
        self.follower_maker = dictionary["follower_maker"]
        self.cost = dictionary["cost"]
        self.total_follower_maker = dictionary["total_follower_maker"]
        self.cost_shown = dictionary["cost_shown"]
        self.cost_multiplier = dictionary["cost_multiplier"]

    def getLevel(self):
        return self.level

    def getFollowerMaker(self):
        return self.follower_maker

    def getCost(self):
        return self.cost

    def getTotalFollowerMaker(self):
        return self.total_follower_maker

    def getCostShown(self):
        return self.cost_shown

    def getCostMultiplier(self):
        return self.cost_multiplier

    def setLevel(self, new_level):
        self.level = new_level

    def setFollowerMaker(self, new_follower_maker):
        self.follower_maker = new_follower_maker

    def setCost(self, new_cost):
        self.cost = new_cost

    def setTotalFollowerMaker(self, new_total_follower_maker):
        self.total_follower_maker = new_total_follower_maker

    def setCostShown(self, new_cost_shown):
        self.cost_shown = new_cost_shown

    def setCostMultiplier(self, new_cost_multiplier):
        self.cost_multiplier = new_cost_multiplier
