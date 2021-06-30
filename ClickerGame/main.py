import sys

from PyQt5 import QtWidgets
import BuildingService
import Ui_MainWindow
import Followers
import UpdateUI

if __name__ == "__main__":
    buildings = BuildingService.BuildingService()
    followers = Followers.Followers()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow.Ui_MainWindow(buildings)
    ui.setupUi(MainWindow)
    update_UI = UpdateUI.UpdateUI(ui, followers, buildings)

    MainWindow.show()
    sys.exit(app.exec_())
