
from src.message import *
import unittest

class TestMessage(unittest.TestCase):
    """test all functions in CLass Message"""

    @classmethod
    def setUpClass(cls):
        print("Message class test start :")
    
    def setUp(self):
        self.h = Header("FIX.4.4", 61, '0', '2', "FIXSIM", "20180109-00:00:03.852")
        self.t = Trailer('055')
        self.heartbeat_msg = Message(self.h, self.t)
        self.new_order_msg = TradeMessage(self.h, self.t, 'TEST1234', '0', 0, '1', '0700', '20180109-07:01:01',
                                        '0', 'QO37NA54U3C8NTYKHDT15N4_0', '0', 100, 0)
        self.execu_order_msg = TradeMessage(self.h, self.t, 'TEST1234', '25', 50, '1', '0700', '20180109-07:01:01',
                                        'F', 'QO37NA54U3C8NTYKHDT15N4_0', '25', 50, 50)
        self.log_on_msg = LogOnMessage(self.h, self.t ,'30')

    @classmethod
    def tearDownClass(cls):
        print("Message class test finished\n")

    def test_header_gets(self):
        self.assertEqual("FIX.4.4", self.h.get_begin_string())
        self.assertEqual(61, self.h.get_body_length())
        self.assertEqual('0', self.h.get_msg_type())
        self.assertEqual('2', self.h.get_msg_seq_num())
        self.assertEqual('FIXSIM', self.h.get_target_comp_id())
        self.assertEqual("20180109-00:00:03.852", self.h.get_sending_time())

    def test_header_sets(self):
        self.h.set_begin_string("FIX.4.5")
        self.h.set_body_length(63)
        self.h.set_msg_type('5')
        self.h.set_msg_seq_num('3')
        self.h.set_target_comp_id('FIXSIMA')
        self.h.set_sending_time("20180109-00:00:04.852")
        self.assertEqual("FIX.4.5", self.h.get_begin_string())
        self.assertEqual(63, self.h.get_body_length())
        self.assertEqual('5', self.h.get_msg_type())
        self.assertEqual('3', self.h.get_msg_seq_num())
        self.assertEqual('FIXSIMA', self.h.get_target_comp_id())
        self.assertEqual("20180109-00:00:04.852", self.h.get_sending_time())

    def test_trailer_gets(self):
        self.assertEqual('055', self.t.get_check_sum())

    def test_trailer_sets(self):
        self.t.set_check_sum('010')
        self.assertEqual('010', self.t.get_check_sum())

    def test_log_on_gets(self):
        self.assertEqual('30', self.log_on_msg.get_heart_beat_int())
        self.assertEqual(True, self.log_on_msg.get_reset_seq_num_flag())

    def test_log_on_sets(self):
        self.log_on_msg.set_heart_beat_int('50')
        self.log_on_msg.set_reset_seq_num_flag(False)
        self.assertEqual('50', self.log_on_msg.get_heart_beat_int())
        self.assertEqual(False, self.log_on_msg.get_reset_seq_num_flag())
    
    def test_trade_message_gets(self):
        self.assertEqual("TEST1234", self.new_order_msg.get_account())
        self.assertEqual('0', self.new_order_msg.get_price())
        self.assertEqual(0, self.new_order_msg.get_quantity())
        self.assertEqual('buy', self.new_order_msg.get_side())
        self.assertEqual('\t0700', self.new_order_msg.get_code())
        self.assertEqual("20180109-07:01:01", self.new_order_msg.get_time())
        self.assertEqual('0', self.new_order_msg.get_exec_type())
        self.assertEqual("QO37NA54U3C8NTYKHDT15N4_0", self.new_order_msg.get_order_id())
        self.assertEqual('0', self.new_order_msg.get_aver_price())
        self.assertEqual(100, self.new_order_msg.get_left_qty())
        self.assertEqual(0, self.new_order_msg.get_sum_qty())


    def test_trade_message_sets(self):
        self.execu_order_msg.set_account('TEST12345')
        self.execu_order_msg.set_price('25')
        self.execu_order_msg.set_quantity(50)
        self.execu_order_msg.set_side('2')
        self.execu_order_msg.set_code(r'\t0922')
        self.execu_order_msg.set_time("20180109-07:01:03")
        self.execu_order_msg.set_exec_type('F')
        self.execu_order_msg.set_order_id("QO37NA54U3C8NTYKHDT15N5_0")
        self.execu_order_msg.set_aver_price('25')
        self.execu_order_msg.set_left_qty(50)
        self.execu_order_msg.set_sum_qty(50)
        self.assertEqual("TEST12345", self.execu_order_msg.get_account())
        self.assertEqual('25', self.execu_order_msg.get_price())
        self.assertEqual(50, self.execu_order_msg.get_quantity())
        self.assertEqual('sell', self.execu_order_msg.get_side())
        self.assertEqual(r'\t0922', self.execu_order_msg.get_code())
        self.assertEqual("20180109-07:01:03", self.execu_order_msg.get_time())
        self.assertEqual('F', self.execu_order_msg.get_exec_type())
        self.assertEqual("QO37NA54U3C8NTYKHDT15N5_0", self.execu_order_msg.get_order_id())
        self.assertEqual('25', self.execu_order_msg.get_aver_price())
        self.assertEqual(50, self.execu_order_msg.get_left_qty())
        self.assertEqual(50, self.execu_order_msg.get_sum_qty())

    def test_order_message_format(self):
        self.assertEqual(['\t0700', 'TEST1234', 100, 'buy', 'QO37NA54U3C8NTYKHDT15N4_0', '20180109-07:01:01'], self.new_order_msg.order_message_format())

    def test_exec_message_format(self):
        self.assertEqual(['\t0700', 'TEST1234', 50, 'buy', 'QO37NA54U3C8NTYKHDT15N4_0', '20180109-07:01:01'], self.execu_order_msg.order_message_format())