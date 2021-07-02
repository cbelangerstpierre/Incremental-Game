class UpdateUI:
    def __init__(self, ui, followers, buildings):
        self.ui = ui
        self.followers = followers
        self.buildings = buildings

    def updateText(self):
        pass

    @staticmethod
    def scientificNumber(number):
        if float(number) >= 10000:
            number = "{:.2f}".format(float(number))
            number = f"{number[0]}.{number[1]}E{len(number) - 4}"

        return number

    def updateFollowers(self):
        self.ui.num_of_followers_label.setText(f"{self.scientificNumber(self.followers.getFollowers())} followers")

    def setCostShownLessThanMax(self, building):
        new_cost_shown = building.getCost()
        for i in range(int(self.ui.num_of_buys_list[self.ui.num_of_buys_number]) - 1):
            new_cost_shown += building.getCost() * building.getCostMultiplier() ** (i + 1)
        new_cost_shown = "{:.2f}".format(new_cost_shown)
        building.setCostShown(new_cost_shown)

    def cannotBuyOneLevel(self, building):
        return float(self.followers.followers) < building.getCost()

    def setCostsAbleToBuyFromBuilding(self, building):
        new_cost_shown = building.getCost()
        last_cost = building.getCost()
        able_to_buy = 1
        while new_cost_shown <= float(self.followers.followers):
            new_cost_shown += last_cost * building.getCostMultiplier()
            last_cost *= building.getCostMultiplier()
            able_to_buy += 1

        return {"new_cost_shown": new_cost_shown, "last_cost": last_cost, "able_to_buy": able_to_buy}

    @staticmethod
    def initCostsAbleToBuy():
        return {"new_cost_shown": 0, "last_cost": 0, "able_to_buy": 1}

    def setLabelAbleToBuy(self, building, variables, num_of_buys_label_list_index):
        building.setCostShown("{:.2f}".format(variables["new_cost_shown"] - variables["last_cost"]))
        self.ui.num_of_buys_label_list[num_of_buys_label_list_index].setText(f"Buy x{variables['able_to_buy'] - 1}")
        num_of_buys_label_list_index += 1

        return num_of_buys_label_list_index

    def setLabelCostAbleToBuy(self):
        building_list_index = 0
        for cost_label in self.ui.cost_label_list:
            cost_label.setText(f"Cost : "
                               f"{self.scientificNumber(self.buildings.building_list[building_list_index].cost_shown)}")
            building_list_index += 1

    def updateNumOfBuysCost(self):
        num_of_buys_label_list_index = 0
        for building in self.buildings.building_list:
            if self.ui.num_of_buys_number != 3:
                self.setCostShownLessThanMax(building)

            else:
                if self.cannotBuyOneLevel(building):
                    variables = self.initCostsAbleToBuy()

                else:
                    variables = self.setCostsAbleToBuyFromBuilding(building)

                num_of_buys_label_list_index = self.setLabelAbleToBuy(building, variables, num_of_buys_label_list_index)

        self.setLabelCostAbleToBuy()

    def OrangeBuildingsBackground(self):
        i = 0
        for building in self.buildings.building_list:
            if float(building.cost_shown) <= float(self.followers.getFollowers()):
                self.ui.building_background_list[i].setStyleSheet("background-color: rgb(193, 119, 0);\n"
                                                                  "border-radius: 10px;\n"
                                                                  "border-width: 2px;\n"
                                                                  "border-style: outset;\n"
                                                                  "border-color:black;")
                i += 1
            else:
                self.ui.building_background_list[i].setStyleSheet("background-color: rgb(114, 114, 114);\n"
                                                                  "border-radius: 10px;\n"
                                                                  "border-width: 2px;\n"
                                                                  "border-style: outset;\n"
                                                                  "border-color:black;")
