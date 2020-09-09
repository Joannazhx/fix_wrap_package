import re

class Order():

    def __init__(self, order_id, code, qty, side, account_num, cum_qty, aver_price, left_qty, price):
        self.__order_id = order_id
        self.__account_num = account_num
        self.__code = code
        self.__last_qty = qty
        self.__left_qty = left_qty
        self.__cum_qty = cum_qty
        self.__aver_price = aver_price
        self.__last_price = price
        self.__side = side
        self.__position = ''
    
    def setPos(self):
        if self.__left_qty == 0:
            self.__position = 'closed'
        else:
            self.__position = 'open'

    def getPos(self):
        return self.__position

    def getPrice(self):
        return self.__last_price

    def setPrice(self, price):
        self.__last_price = price

    def getAccountNum(self):
        return self.__account_num

    def setAverPrice(self, aver_price):
        self.__aver_price = aver_price

    def getAverPrice(self):
        return self.__aver_price

    def setQty(self, qyt):
        self.__last_qty = qyt

    def getQty(self):
        return self.__last_qty

    def setCumQty(self, cum_qyt):
        self.__cum_qty = cum_qyt

    def getCumQty(self):
        return self.__cum_qty

    def getCode(self):
        return str(self.__code)
    
    def getSide(self):
        return self.__side

    def getOrderId(self):
        return self.__order_id

    def getLeftQty(self):
        return self.__left_qty
    
    def setLeftQty(self, left_qty):
        self.__left_qty = left_qty

    def orderHead(self):
        name_space = self.__dict__.keys()
        names = []
        for name in name_space:
            name = re.sub('^__', '', name.split('__')[1])
            names.append(name)
        return names

    def printOrder(self):
        headers = self.orderHead()
        out_values = [self.getOrderId(), self.getAccountNum(), self.getCode(), self.getQty(),
            self.getLeftQty(), self.getCumQty(), self.getAverPrice(),  self.getPrice(), self.getSide(), self.getPos()]
        out_str = ""
        for i in range(len(headers)):
            out_str += ( headers[i] + " : " + str(out_values[i]) + " | ")
        print(out_str)