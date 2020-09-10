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
        self.assertEqual(False,  self.order_pool.serachOrder('QO37NA54U3C8NTYKHDT15N4_0'))
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
        self.order_pool.addOrder(order)
        self.assertEqual(order,  self.order_pool.serachOrder(order.getOrderId()))

    def test_add_order_to_pool(self):
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
        self.order_pool.addOrder(order)
        self.assertEqual(order, self.order_pool.serachOrder(order.getOrderId()))
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0800', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
        self.order_pool.addOrder(order)
        self.assertNotEqual(order, self.order_pool.serachOrder(order.getOrderId()))

    def test_update_order_to_pool(self):
        # return false when order not send by client
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 0, 'buy', 'TEST1234', 0, '0', 100, '0')
        self.order_pool.updateOrder(order)
        self.assertEqual(False, self.order_pool.serachOrder(order.getOrderId()))

        #add then update the order
        self.order_pool.addOrder(order)
        order = Order('QO37NA54U3C8NTYKHDT15N4_0', '\t0700', 50, 'buy', 'TEST1234', 50, '25', 50, '25')
        self.order_pool.updateOrder(order)
        self.assertEqual(order.getOrderId(), self.order_pool.serachOrder(order.getOrderId()).getOrderId())
        self.assertEqual(order.getAccountNum(), self.order_pool.serachOrder(order.getOrderId()).getAccountNum())
        self.assertEqual(order.getAverPrice(), self.order_pool.serachOrder(order.getOrderId()).getAverPrice())
        self.assertEqual(order.getCumQty(), self.order_pool.serachOrder(order.getOrderId()).getCumQty())
        self.assertEqual(order.getLeftQty(), self.order_pool.serachOrder(order.getOrderId()).getLeftQty())
        self.assertEqual(order.getQty(), self.order_pool.serachOrder(order.getOrderId()).getQty())

