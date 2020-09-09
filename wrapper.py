from reader import *
from orderPool import *
import csv
HEADEREXECU = ["Stock Code","Transaction Quantity","Transaction Price", "Transaction Side", "Account", "Transaction Reference ID", "Transaction Time"]
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
        for line in lines:
            if line[0] == '#':
                continue
            self.__mess = self.__reader.read_line(line)
            self.updateOrderPool()
        global HEADEREXECU
        self.csv_write("execu.csv", HEADEREXECU, self.__exec)


    def updateOrderPool(self):
        if(self.__mess.__class__.__name__ == 'TradeMessage'):
            # add order into customer order and orderpool
            # print(self.__mess.getExecType())
            order = Order(self.__mess.getOrderId(), self.__mess.getCode(), self.__mess.getQuantity(), 
                                    self.__mess.getSide(), self.__mess.getAccount())
            if(self.__mess.getExecType() == '0'):
                self.__order_pool.addOrder(order)
                if not order.getAccountNum() in self.__customer_orders:
                    self.__customer_orders[order.getAccountNum()] = []
                self.__customer_orders[order.getAccountNum()].append(self.__mess.execMessageFormat())
                print(self.__mess.execMessageFormat())
            
            elif (self.__mess.getExecType() == 'F'):
                self.__exec.append(self.__mess.execMessageFormat())


    def csv_write(self, filepath, header, rows):
        print(rows)
        with open(filepath,"w") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(rows)