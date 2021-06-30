class UpdateUI:
    def __init__(self, ui, followers, buildings):
        self.ui = ui
        self.followers = followers
        self.buildings = buildings

    def updateText(self):
        #self.ui.follower_maker_label3.setText("Hello")
        #print(self.ui.follower_maker_label3.setText(""))
        print(self.followers)
        print(self.buildings.speak_to_someone.name, "5")
