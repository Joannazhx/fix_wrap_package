import csv, os, sys
import os, sys
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)
from reader import *
from order_pool import *
from message import *
from const import *


class Wrapper():

    def __init__(self, file_path, out_dir):
        self.__file = file_path 
        self.__reader = Reader(self.__file)
        self.__mess = {}
        self.__order_pool = OrderPool()
        self.__out_execu = os.path.abspath(os.path.join(out_dir, EXECUFILE))
        self.__out_order = os.path.abspath(os.path.join(out_dir, ORDERFILE))
        self.__out_account = os.path.abspath(os.path.join(out_dir, ACCOUNTFILE))

    def start(self):
        lines = self.__reader.read_log()
        self.csv_write(self.__out_execu, HEADEREXECU, "w")
        self.csv_write(self.__out_order, HEADERORDER, "w")
        for line in lines:
            if line[0] == '#':
                continue
            self.__mess = self.__reader.read_line(line)
            order = self.updateOrder()
            if not order is None:    
                self.updateOrderPool(order)
                order.setPos()
                print((self.__order_pool.serachOrder(order.getOrderId())).printOrder())
        self.orderPoolOut()
            
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
            self.csv_write(self.__out_order, self.__mess.orderMessageFormat(), "a+")
                
            
        elif (self.__mess.getExecType() == 'F'):
            self.__order_pool.updateOrder(order)
            print("execu order message :{}".format(self.__mess.execMessageFormat()))
            self.csv_write(self.__out_execu, self.__mess.execMessageFormat(), "a+")

    def orderPoolOut(self):
        rows = self.__order_pool.acctPos()
        self.csv_write(self.__out_account, [], "w")
        for row in rows:
            self.csv_write(self.__out_account, row, "a+")
            # print(row)
                

    def csv_write(self, filepath, row, writer):
        with open(filepath, writer) as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(row)
