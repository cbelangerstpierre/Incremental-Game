import sys
import threading
from PyQt5 import QtWidgets
from generators import first_generator, second_generator, third_generator
from money_class import money
from gui import Ui_IncrementalGame


def every_tenth_of_second():
    threading.Timer(0.1, every_tenth_of_second).start()
    new_money = "{:.1f}".format(float(money.getMoney()) + money.getMoneyMaker() / 10)
    money.setMoney(new_money)
    ui.total_money.setText(f"You have {money.getMoney()} dollars")
    ui.money_making.setText(f"You are doing {money.getMoneyMaker()} dollars per second")
    ui.label_generator_price1.setText(f"{first_generator.getPrice()}$")
    ui.label_generator_price2.setText(f"{second_generator.getPrice()}$")
    ui.label_generator_price3.setText(f"{third_generator.getPrice()}$")
    ui.label_generator_price1.adjustSize()
    ui.label_generator_price2.adjustSize()
    ui.label_generator_price3.adjustSize()
    ui.label_generator_owned1.setText(f"You own {first_generator.getNumberOwned()}")
    ui.label_generator_owned2.setText(f"You own {second_generator.getNumberOwned()}")
    ui.label_generator_owned3.setText(f"You own {third_generator.getNumberOwned()}")
    ui.label_generator_owned1.adjustSize()
    ui.label_generator_owned2.adjustSize()
    ui.label_generator_owned3.adjustSize()


if __name__ == '__main__':
    print("Hello")
    print(money.getMoneyMaker())
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_IncrementalGame()
    ui.setupUi(MainWindow)
    every_tenth_of_second()
    MainWindow.show()
    sys.exit(app.exec_())
