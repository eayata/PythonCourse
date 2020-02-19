import random

class Portfolio():

    def __init__(self):
        self.cash = 0.0
        self.stock = {}
        self.mfund = {}
        self.hist = []

    def history(self):
        return self.hist

    def addCash(self, amount):
        amount = float(amount)
        self.cash = self.cash + amount
        self.hist.append("Cash deposit %s" %amount)

    def withdrawCash(self, amount):
        self.addCash(-amount)
        self.hist.append("Cash withdrawal %s" % amount)

    def buyStock(self, amount, name):

        buy_price = name.price
        sell_price = random.uniform((0.5 * buy_price), (1.5 * buy_price))
        if amount <= 0 or (self.cash-amount*buy_price) <= 0:
            print("Can not buy %a since there is not enough cash or given amount is negative" %name.name)
            self.hist.append("Invalid transaction")
        else:
            if name.name in self.stock:
                self.stock[name.name] = self.stock[name.name] + amount
            else:
                self.stock[name.name] = amount
            self.cash = self.cash-(buy_price * amount)
            self.hist.append("Bought %s stocks %s" %(amount,name.name))


    def sellStock(self, amount, name):

        buy_price = name.price
        sell_price = random.uniform((0.5 * buy_price), (1.5 * buy_price))
        if name.name in self.stock:
            self.stock[name.name] = self.stock[name.name] - amount
        else:
            self.stock[name.name] = amount
        self.cash=self.cash+ (sell_price * amount)
        self.hist.append("Sold %s stocks %s" % (amount, name.name))

    def buyMutualFund(self,amount,name):
        sell_price = random.uniform(0.9,1.2)
        if amount <= 0 or self.cash-amount <=0:
            print("Can not buy %a since there is not enough cash or given amount is negative" %name.name)
            self.hist.append["Invalid transaction"]
        else:
            if name.name in self.mfund:
                self.mfund[name.name] = self.mfund[name.name] + amount
            else:
                self.mfund[name.name] = amount
            self.cash = self.cash-(amount)
            self.hist.append("Bought %s mutual funds %s" % (amount, name.name))

    def sellMutualFund(self, amount,name):

        sell_price = random.uniform(0.9, 1.2)
        if name.name in self.mfund:
            self.mfund[name.name] = self.mfund[name.name] - amount
        else:
            self.mfund[name.name] = amount
        self.cash = self.cash-(amount)
        self.hist.append("Sold %s mutual funds %s" % (amount, name.name))

    def __str__(self):
        return "Cash: %s \nStock: %s \n Mutual Fund: %s" %(self.cash,self.stock,self.mfund)


class Stock():

    def __init__(self,price,name):
        self.price = 0.0
        self.name = name
        self.price = price
        self.sellprice = random.uniform((0.5 * price), (1.5 * price))

    def name(self):
        return self.name, self.price

    def __str__(self):
        return "Name: %s \nPrice: %s  \n " % (self.name, self.price)

class MutualFund():

    def __init__(self, name):
        self.name = name
        self.share = 0.0
        self.sellprice = random.uniform(0.9,1.2)

    def __str__(self):
        return "\n Cash: %s \n Stock: %s  \n " % (self.name, self.share)
#test
portfolio = Portfolio()
portfolio.addCash(500)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.withdrawCash(10)
print(portfolio)
portfolio.history()

