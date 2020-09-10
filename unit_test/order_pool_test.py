import sys
# sys.path.append("..")
from src.order_pool import *
import unittest

class TestOrderPool(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("OrderPool class test start :")
    
    def setUp(self):
        self.order_pool = OrderPool()
    
    @classmethod
    def tearDownClass(cls):
        print("OrderPool class test finished\n")

    def test_serach_order_pool(self):
        self.assertEqual(False,  self.order_pool.serach_order('QO37NA54U3C8NTYKHDT15N4_0'))
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
        self.order_pool.add_order(order)
        self.assertEqual(order,  self.order_pool.serach_order(order.get_order_id()))

    def test_add_order_to_pool(self):
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
        self.order_pool.add_order(order)
        self.assertEqual(order, self.order_pool.serach_order(order.get_order_id()))
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0800', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
        self.order_pool.add_order(order)
        self.assertNotEqual(order, self.order_pool.serach_order(order.get_order_id()))

    def test_update_order_to_pool(self):
        # return false when order not send by client
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
        self.order_pool.update_order(order)
        self.assertEqual(False, self.order_pool.serach_order(order.get_order_id()))

        #add then update the order
        self.order_pool.add_order(order)
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 50, 'buy', 'TEST1234', 50, '25', 50, '25')
        self.order_pool.update_order(order)
        self.assertEqual(order.get_order_id(), self.order_pool.serach_order(order.get_order_id()).get_order_id())
        self.assertEqual(order.get_account_num(), self.order_pool.serach_order(order.get_order_id()).get_account_num())
        self.assertEqual(order.get_aver_price(), self.order_pool.serach_order(order.get_order_id()).get_aver_price())
        self.assertEqual(order.get_cum_qty(), self.order_pool.serach_order(order.get_order_id()).get_cum_qty())
        self.assertEqual(order.get_left_qty(), self.order_pool.serach_order(order.get_order_id()).get_left_qty())
        self.assertEqual(order.get_qty(), self.order_pool.serach_order(order.get_order_id()).get_qty())

