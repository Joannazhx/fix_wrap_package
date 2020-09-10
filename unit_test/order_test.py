import sys
sys.path.append("..")
from src.order import *
import unittest

class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Reader class test start :")

    def setUp(self):
        self.order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
    
    @classmethod
    def tearDownClass(cls):
        print("Order class test finished")

    def test_order_gets(self):
        self.assertEqual('QO37NA54U3C8NTYKHDT15N4_0', self.order.getOrderId())
        self.assertEqual('\t0700', self.order.getCode())
        self.assertEqual(0, self.order.getQty())
        self.assertEqual('buy', self.order.getSide())
        self.assertEqual('TEST1234', self.order.getAccountNum())
        self.assertEqual(0, self.order.getCumQty())
        self.assertEqual('0', self.order.getAverPrice())
        self.assertEqual(100, self.order.getLeftQty())
        self.assertEqual('0', self.order.getPrice())

    def test_order_gets(self):
        self.order.setOrderId('QO37NA54U3C8NTYKHDT15N5_0')
        self.order.setCode('\t0922')
        self.order.setQty(50)
        self.order.setSide('2')
        self.order.setAccountNum('TEST12345')
        self.order.setCumQty(50)
        self.order.setAverPrice('25')
        self.order.setLeftQty(50)
        self.order.setPrice('25')
        self.assertEqual('QO37NA54U3C8NTYKHDT15N5_0', self.order.getOrderId())
        self.assertEqual('\t0922', self.order.getCode())
        self.assertEqual(50, self.order.getQty())
        self.assertEqual('sell', self.order.getSide())
        self.assertEqual('TEST12345', self.order.getAccountNum())
        self.assertEqual(50, self.order.getCumQty())
        self.assertEqual('25', self.order.getAverPrice())
        self.assertEqual(50, self.order.getLeftQty())
        self.assertEqual('25', self.order.getPrice())

    def test_order_headers(self):
        self.assertEqual(['order_id', 'account_num', 'code', 'last_qty', 'left_qty', 'cum_qty', 'aver_price', 'last_price', 'side', 'position'], 
                            self.order.orderHead())
        
    def test_order_print_order(self):
        self.assertEqual("order_id : QO37NA54U3C8NTYKHDT15N4_0 | account_num : TEST1234 | code : 	0700 | last_qty : 0 | left_qty : 100 | cum_qty : 0 | aver_price : 0 | last_price : 0 | side : buy | position :  | ", 
                            self.order.printOrder())

    def test_order_value(self):
        self.assertEqual(['QO37NA54U3C8NTYKHDT15N4_0' ,'TEST1234', '\t0700' , 0 , 100 , 0 , '0' , '0' , 'buy' , ''],
            self.order.orderValue())                        

    def test_order_set_position(self):
        self.order.setPos()
        self.assertEqual('open', self.order.getPos())
        self.order.setLeftQty(0)
        self.order.setPos()
        self.assertEqual('closed', self.order.getPos())