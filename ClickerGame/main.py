import sys
import threading

from PyQt5 import QtWidgets
import BuildingService
import Ui_MainWindow
import Followers
import UpdateUI


def every_tenth_of_second():
    threading.Timer(0.1, every_tenth_of_second).start()
    new_followers = "{:.1f}".format(float(followers.getFollowers()) + followers.getFollowersMaker() / 10)
    followers.setFollowers(new_followers)
    update_UI.updateFollowers()
    # update_UI.OrangeBuildingsBackground()    ### Doesn't work
    if ui.num_of_buys_number == 3:
        update_UI.updateNumOfBuysCost()


if __name__ == "__main__":
    buildings = BuildingService.BuildingService()
    followers = Followers.Followers()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow.Ui_MainWindow(buildings, followers)
    ui.setupUi(MainWindow)
    update_UI = UpdateUI.UpdateUI(ui, followers, buildings)
    ui.setUpdateUI(update_UI)
    every_tenth_of_second()
    MainWindow.show()
    sys.exit(app.exec_())
