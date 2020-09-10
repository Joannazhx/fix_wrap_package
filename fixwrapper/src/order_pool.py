import os, sys
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)
from order import *

class OrderPool():
    def __init__(self):
        self.__orders = {}

    def serachOrder(self, order_id):
        if order_id in self.__orders:
            return self.__orders[order_id]
        else:
            return False
    
    def addOrder(self, order):
        order_locate = self.serachOrder(order.getOrderId())
        if not order_locate:
            order.setPos()
            self.__orders[order.getOrderId()] = order
        else:
            print("Error orderId, not unique")
            pass

    def updateOrder(self, order):
        order_locate = self.serachOrder(order.getOrderId())
        if order_locate:
            if(order_locate.getLeftQty() < order.getQty()):
                print("Error Qty, larger than left quantity")
                return False
            order_locate.setAverPrice(order.getAverPrice())
            order_locate.setPrice(order.getPrice())
            order_locate.setCumQty(order.getQty() + order_locate.getCumQty())
            order_locate.setLeftQty(order.getLeftQty())
            order_locate.setQty(order.getQty())
            order_locate.setPos()
            self.__orders[order.getOrderId()] = order_locate

    def acctPos(self):
        order_rows = []
        for order_id in self.__orders:
            if len(order_rows) == 0:
                order_rows.append(self.__orders[order_id].orderHead())
            order_rows.append(self.__orders[order_id].orderValue())
        return order_rows


