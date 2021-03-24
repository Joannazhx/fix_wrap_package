import sys
sys.path.append("..")
<<<<<<< HEAD
from fixwrapper.order import *
=======
from src.order import *
>>>>>>> 47b13e6a5c9952fc79f94b25b28e9a9a287c0386
import unittest

class TestOrder(unittest.TestCase):
    """test all functions in CLass Order"""

    @classmethod
    def setUpClass(cls):
        print("Order class test start :")

    def setUp(self):
        self.order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
    
    @classmethod
    def tearDownClass(cls):
        print("Order class test finished")

    def test_order_gets(self):
        self.assertEqual('QO37NA54U3C8NTYKHDT15N4_0', self.order.get_order_id())
        self.assertEqual('\t0700', self.order.get_code())
        self.assertEqual(0, self.order.get_qty())
        self.assertEqual('buy', self.order.get_side())
        self.assertEqual('TEST1234', self.order.get_account_num())
        self.assertEqual(0, self.order.get_cum_qty())
        self.assertEqual('0', self.order.get_aver_price())
        self.assertEqual(100, self.order.get_left_qty())
        self.assertEqual('0', self.order.get_price())

    def test_order_gets(self):
        self.order.set_order_id('QO37NA54U3C8NTYKHDT15N5_0')
        self.order.set_code('\t0922')
        self.order.set_qty(50)
        self.order.set_side('2')
        self.order.set_account_num('TEST12345')
        self.order.set_cum_qty(50)
        self.order.set_aver_price('25')
        self.order.set_left_qty(50)
        self.order.set_price('25')
        self.assertEqual('QO37NA54U3C8NTYKHDT15N5_0', self.order.get_order_id())
        self.assertEqual('\t0922', self.order.get_code())
        self.assertEqual(50, self.order.get_qty())
        self.assertEqual('sell', self.order.get_side())
        self.assertEqual('TEST12345', self.order.get_account_num())
        self.assertEqual(50, self.order.get_cum_qty())
        self.assertEqual('25', self.order.get_aver_price())
        self.assertEqual(50, self.order.get_left_qty())
        self.assertEqual('25', self.order.get_price())

    def test_order_headers(self):
        self.assertEqual(['order_id', 'account_num', 'code', 'last_qty', 'left_qty', 'cum_qty', 'aver_price', 'last_price', 'side', 'position'], 
                            self.order.order_head())
        
    def test_order_print_order(self):
        self.assertEqual("order_id : QO37NA54U3C8NTYKHDT15N4_0 | account_num : TEST1234 | code : 	0700 | last_qty : 0 | left_qty : 100 | cum_qty : 0 | aver_price : 0 | last_price : 0 | side : buy | position :  | ", 
                            self.order.print_order())

    def test_order_value(self):
        self.assertEqual(['QO37NA54U3C8NTYKHDT15N4_0' ,'TEST1234', '\t0700' , 0 , 100 , 0 , '0' , '0' , 'buy' , ''],
            self.order.order_value())                        

    def test_order_set_position(self):
        self.order.set_pos()
        self.assertEqual('open', self.order.get_pos())
        self.order.set_left_qty(0)
        self.order.set_pos()
        self.assertEqual('closed', self.order.get_pos())