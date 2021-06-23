from PyQt5 import QtCore, QtGui, QtWidgets
from generators import first_generator, second_generator, third_generator
from money_class import money


def generator1_clicked():
    if money.getMoney() >= first_generator.price:
        new_money_maker = money.getMoneyMaker() + first_generator.boost
        money.setMoneyMaker(new_money_maker)
        money.setMoney(money.getMoney() - first_generator.price)
        first_generator.setPrice(round(first_generator.getPrice() * 1.5))
        first_generator.setNumberOwned(first_generator.getNumberOwned() + 1)
    else:
        pass


def generator2_clicked():
    if money.getMoney() >= second_generator.price:
        new_money_maker = money.getMoneyMaker() + second_generator.boost
        money.setMoneyMaker(new_money_maker)
        money.setMoney(money.getMoney() - second_generator.price)
        second_generator.setPrice(round(second_generator.getPrice() * 1.5))
        second_generator.setNumberOwned(second_generator.getNumberOwned() + 1)
    else:
        pass


def generator3_clicked():
    if money.getMoney() >= third_generator.price:
        new_money_maker = money.getMoneyMaker() + third_generator.boost
        money.setMoneyMaker(new_money_maker)
        money.setMoney(money.getMoney() - third_generator.price)
        third_generator.setPrice(round(third_generator.getPrice() * 1.5))
        third_generator.setNumberOwned(third_generator.getNumberOwned() + 1)
    else:
        pass


class Ui_IncrementalGame(object):
    def setupUi(self, IncrementalGame):
        IncrementalGame.setObjectName("Incremental Game")
        IncrementalGame.resize(800, 544)
        self.centralwidget = QtWidgets.QWidget(IncrementalGame)
        self.centralwidget.setObjectName("centralwidget")
        self.third_generator_button = QtWidgets.QPushButton(self.centralwidget)
        self.third_generator_button.setGeometry(QtCore.QRect(580, 410, 191, 61))
        self.third_generator_button.setText("")
        self.third_generator_button.setObjectName("button3")
        self.second_generator_button = QtWidgets.QPushButton(self.centralwidget)
        self.second_generator_button.setGeometry(QtCore.QRect(315, 410, 191, 61))
        self.second_generator_button.setText("")
        self.second_generator_button.setObjectName("button2")
        self.first_generator_button = QtWidgets.QPushButton(self.centralwidget)
        self.first_generator_button.setGeometry(QtCore.QRect(30, 410, 191, 61))
        self.first_generator_button.setAutoFillBackground(False)
        self.first_generator_button.setText("")
        self.first_generator_button.setObjectName("button1")
        self.label_generator_title1 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_title1.setGeometry(QtCore.QRect(80, 410, 91, 31))
        self.label_generator_title1.setObjectName("label_generator_title1")
        self.label_generator_boost1 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_boost1.setGeometry(QtCore.QRect(110, 430, 31, 16))
        self.label_generator_boost1.setObjectName("label_generator_boost1")
        self.label_generator_price1 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_price1.setGeometry(QtCore.QRect(110, 450, 31, 16))
        self.label_generator_price1.setObjectName("label_generator_price1")
        self.label_generator_owned1 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_owned1.setGeometry(QtCore.QRect(95, 385, 60, 30))
        self.label_generator_owned1.setObjectName("label_generator_owned1")
        self.total_money = QtWidgets.QLabel(self.centralwidget)
        self.total_money.setGeometry(QtCore.QRect(0, 70, 800, 81))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.total_money.setFont(font)
        self.total_money.setObjectName("total_money")
        self.label_generator_title2 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_title2.setGeometry(QtCore.QRect(360, 410, 111, 31))
        self.label_generator_title2.setObjectName("label_generator_title2")
        self.label_generator_boost2 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_boost2.setGeometry(QtCore.QRect(390, 430, 41, 16))
        self.label_generator_boost2.setObjectName("label_generator_boost2")
        self.label_generator_price2 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_price2.setGeometry(QtCore.QRect(400, 450, 31, 16))
        self.label_generator_price2.setObjectName("label_generator_price2")
        self.label_generator_owned2 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_owned2.setGeometry(QtCore.QRect(385, 385, 60, 30))
        self.label_generator_owned2.setObjectName("label_generator_owned2")
        self.money_making = QtWidgets.QLabel(self.centralwidget)
        self.money_making.setGeometry(QtCore.QRect(160, 200, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.money_making.setFont(font)
        self.money_making.setObjectName("money_making")
        self.label_generator_title3 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_title3.setGeometry(QtCore.QRect(630, 410, 101, 31))
        self.label_generator_title3.setObjectName("label_generator_title3")
        self.label_generator_boost3 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_boost3.setGeometry(QtCore.QRect(650, 430, 51, 16))
        self.label_generator_boost3.setObjectName("label_generator_boost3")
        self.label_generator_price3 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_price3.setGeometry(QtCore.QRect(661, 450, 31, 16))
        self.label_generator_price3.setObjectName("label_generator_price3")
        self.label_generator_owned3 = QtWidgets.QLabel(self.centralwidget)
        self.label_generator_owned3.setGeometry(QtCore.QRect(645, 385, 60, 30))
        self.label_generator_owned3.setObjectName("label_generator_owned3")
        IncrementalGame.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IncrementalGame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        IncrementalGame.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IncrementalGame)
        self.statusbar.setObjectName("statusbar")
        IncrementalGame.setStatusBar(self.statusbar)
        self.actionRestart = QtWidgets.QAction(IncrementalGame)
        self.actionRestart.setObjectName("actionRestart")
        self.menuOptions.addAction(self.actionRestart)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(IncrementalGame)
        QtCore.QMetaObject.connectSlotsByName(IncrementalGame)

        self.actionRestart.triggered.connect(lambda: self.reset_clicked())

        self.first_generator_boost = 1
        self.second_generator_boost = 10
        self.third_generator_boost = 100
        self.first_generator_button.clicked.connect(generator1_clicked)
        self.second_generator_button.clicked.connect(generator2_clicked)
        self.third_generator_button.clicked.connect(generator3_clicked)

    def retranslateUi(self, IncrementalGame):
        _translate = QtCore.QCoreApplication.translate
        IncrementalGame.setWindowTitle(_translate("IncrementalGame", "Incremental Game"))
        self.label_generator_title1.setText(_translate("IncrementalGame", "First Generator"))
        self.label_generator_boost1.setText(_translate("IncrementalGame", "+ 1/s"))
        self.label_generator_price1.setText(_translate("IncrementalGame", f"{first_generator.price}$"))
        self.label_generator_price1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_generator_price1.adjustSize()
        self.label_generator_owned1.setText(_translate("IncrementalGame", f"You own {first_generator.number_owned}"))
        self.label_generator_owned1.adjustSize()
        self.total_money.setText(_translate("IncrementalGame", f"You have {money.getMoney()} dollars"))
        self.total_money.setAlignment(QtCore.Qt.AlignCenter)
        self.label_generator_title2.setText(_translate("IncrementalGame", "Second Generator"))
        self.label_generator_boost2.setText(_translate("IncrementalGame", "+ 10/s"))
        self.label_generator_price2.setText(_translate("IncrementalGame", f"{second_generator.price}$"))
        self.label_generator_price2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_generator_price2.adjustSize()
        self.label_generator_owned2.setText(_translate("IncrementalGame", f"You own {second_generator.number_owned}"))
        self.label_generator_owned2.adjustSize()
        self.money_making.setText(_translate("IncrementalGame", f"You are doing {money.getMoneyMaker()} dollars per "
                                                                f"second"))
        self.money_making.setAlignment(QtCore.Qt.AlignCenter)
        self.label_generator_title3.setText(_translate("IncrementalGame", "Third Generator"))
        self.label_generator_boost3.setText(_translate("IncrementalGame", "+ 100/s"))
        self.label_generator_price3.setText(_translate("IncrementalGame", f"{third_generator.price}$"))
        self.label_generator_price3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_generator_price3.adjustSize()
        self.label_generator_owned3.setText(_translate("IncrementalGame", f"You own {third_generator.number_owned}"))
        self.label_generator_owned3.adjustSize()
        self.menuOptions.setTitle(_translate("IncrementalGame", "Options"))
        self.actionRestart.setText(_translate("IncrementalGame", "Restart"))
        self.actionRestart.setShortcut(_translate("IncrementalGame", "Ctrl+R"))

    @staticmethod
    def reset_clicked():
        money.setMoney(10)
        money.setMoneyMaker(0)
        first_generator.price = 10
        first_generator.boost = 1
        first_generator.number_owned = 0
        second_generator.price = 200
        second_generator.boost = 10
        second_generator.number_owned = 0
        third_generator.price = 3000
        third_generator.boost = 100
        third_generator.number_owned = 0
