class Order():


    def __init__(self, order_id, code, qty, side, account_num):
        self.__order_id = order_id
        self.__account_num = account_num
        self.__code = code
        self.__qty = qty
        self.__cum_qty = 0
        self.__aver_price = 0
        self.__side = side

    def getAccountNum(self):
        return self.__account_num

    def setAverPrice(self, aver_price):
        self.__aver_price = aver_price

    def getAverPrice(self):
        return self.__aver_price

    def setQty(self, qyt):
        self.__qty = qyt

    def setCumQty(self, cum_qyt):
        self.__cum_qty = cum_qyt

    def getQty(self):
        return self.__qty

    def getCUmQty(self):
        return self.__cum_qty

    def getCode(self):
        return str(self.__code)
    
    def getSide(self):
        return __side

    def getOrderId(self):
        return self.__order_id

    def setProfit(self, profit):
        self.__profit = profit


