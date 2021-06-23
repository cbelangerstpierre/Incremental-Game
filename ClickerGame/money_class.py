class Money:
    def __init__(self):
        self.money = 10
        self.money_maker = 0

    def setMoney(self, new_money):
        self.money = new_money

    def setMoneyMaker(self, new_money_maker):
        self.money_maker = new_money_maker

    def getMoney(self):
        return float(self.money)

    def getMoneyMaker(self):
        return float(self.money_maker)


money = Money()
