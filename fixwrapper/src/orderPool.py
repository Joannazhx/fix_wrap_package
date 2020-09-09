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
            self.__orders[order.getOrderId()] = order
        else:
            print("Error orderId, not unique")

    def updateOrder(self, order):
        order_locate = self.serachOrder(order.getOrderId())
        if order_locate:
            if(order_locate.getQty() > order.getLeftQty()):
                print("Error Qty, larger than left quantity")
                return
            order_locate.setAverPrice(order.getAverPrice())
            order_locate.setCumQty(order.getCumQty())
            order_locate.setLeftQty(order.getLeftQty())
            self.__orders[order.getOrderId()] = order_locate

