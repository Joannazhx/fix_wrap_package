from reader import *
from orderPool import *
import csv

HEADEREXECU = ["Stock Code","Transaction Quantity","Transaction Price", "Transaction Side", "Account", "Transaction Reference ID", "Transaction Time"]
HEADERORDER = ["Stock Code","Account","Total Quantity", "Transaction Side", "Transaction Reference ID", "Transaction Time"]


class Wrapper():

    def __init__(self):
        self.__file = "/Users/joanna/Desktop/jobs/OnGoing/quantifeed/FIX.09-Jan-2018.log"
        self.__reader = Reader(self.__file)
        self.__mess = {}
        self.__order_pool = OrderPool()
        self.__customer_orders = {}
        self.__exec = []

    def start(self):
        lines = self.__reader.read_log()
        global HEADEREXECU
        global HEADERORDER
        self.csv_write("execu.csv", HEADEREXECU, "w")
        self.csv_write("orders.csv", HEADERORDER, "w")
        for line in lines:
            if line[0] == '#':
                continue
            self.__mess = self.__reader.read_line(line)
            order = self.updateOrder()
            if not order is None:    
                self.updateOrderPool(order)
                order.setPos()
                order.printOrder()

            
    def updateOrder(self):
        if(self.__mess.__class__.__name__ == 'TradeMessage'):
            # add order into customer order and orderpool
            order = Order(self.__mess.getOrderId(), self.__mess.getCode(), self.__mess.getQuantity(), self.__mess.getSide(), 
                            self.__mess.getAccount(), self.__mess.getSumQty(), self.__mess.getAverPrice(), self.__mess.getLeftQty(),
                            self.__mess.getPrice())
            return order

    def updateOrderPool(self, order):
        if(self.__mess.getExecType() == '0'):
            self.__order_pool.addOrder(order)
            print("receive order mesaage :{}".format(self.__mess.orderMessageFormat()))
            self.csv_write("orders.csv", self.__mess.orderMessageFormat(), "a+")
                
            
        elif (self.__mess.getExecType() == 'F'):
            self.__order_pool.updateOrder(order)
            print("execu order message :{}".format(self.__mess.execMessageFormat()))
            self.csv_write("execu.csv", self.__mess.execMessageFormat(), "a+")
                

    def csv_write(self, filepath, row, writer):
        with open(filepath, writer) as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(row)
