import sys

from PyQt5 import QtWidgets
import buildingService
import Ui_MainWindow
import Followers
import UpdateUI

if __name__ == "__main__":
    buildings = buildingService.BuildingService()
    followers = Followers.Followers()
    update_UI = UpdateUI.UpdateUI()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
