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

    def updateNumOfBuysCost(self):
        if self.ui.num_of_buys_number != 3:
            for building in self.buildings.building_list:
                # function
                new_cost_shown = building.getCost()
                for i in range(int(self.ui.num_of_buys_list[self.ui.num_of_buys_number]) - 1):
                    new_cost_shown += building.getCost() * building.getCostMultiplier() ** (i + 1)
                new_cost_shown = "{:.2f}".format(new_cost_shown)
                building.setCostShown(new_cost_shown)
                # end function

        else:
            i = 0
            for building in self.buildings.building_list:

                # function
                if float(self.followers.followers) < building.getCost():
                    # function
                    print(building.getCost())
                    new_cost_shown = 0
                    last_cost = 0
                    able_to_buy = 1
                    # end function
                else:
                    # function
                    new_cost_shown = building.getCost()
                    last_cost = building.getCost()
                    able_to_buy = 1
                    while new_cost_shown <= float(self.followers.followers):
                        new_cost_shown += last_cost * building.getCostMultiplier()
                        last_cost *= building.getCostMultiplier()
                        able_to_buy += 1
                    # end function
                building.setCostShown("{:.2f}".format(new_cost_shown - last_cost))
                self.ui.num_of_buys_label_list[i].setText(f"Buy x{able_to_buy - 1}")
                i += 1
                # end function

        i = 0
        for cost_label in self.ui.cost_label_list:
            cost_label.setText(f"Cost : {self.scientificNumber(self.buildings.building_list[i].cost_shown)}")
            i += 1

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
