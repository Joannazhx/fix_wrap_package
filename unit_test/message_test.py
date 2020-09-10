import sys
sys.path.append("..")
from src.message import *
import unittest

class TestMessage(unittest.TestCase):

    def setUp(self):
        self.h = Header("FIX.4.4", 61, '0', '2', "FIXSIM", "20180109-00:00:03.852")
        self.t = Trailer('055')
        self.heartbeat_msg = Message(self.h, self.t)
        self.new_order_msg = TradeMessage(self.h, self.t, 'TEST1234', '0', 0, '1', '0700', '20180109-07:01:01',
                                        '0', 'QO37NA54U3C8NTYKHDT15N4_0', '0', 100, 0)
        self.execu_order_msg = TradeMessage(self.h, self.t, 'TEST1234', '25', 50, '1', '0700', '20180109-07:01:01',
                                        'F', 'QO37NA54U3C8NTYKHDT15N4_0', '25', 50, 50)
        self.log_on_msg = LogOnMessage(self.h, self.t ,'30')

    def tearDown(self):
        pass

    def test_header_gets(self):
        self.assertEqual("FIX.4.4", self.h.getBeginString())
        self.assertEqual(61, self.h.getBodyLength())
        self.assertEqual('0', self.h.getMsgType())
        self.assertEqual('2', self.h.getMsgSeqNum())
        self.assertEqual('FIXSIM', self.h.getTargetCompId())
        self.assertEqual("20180109-00:00:03.852", self.h.getSendingTime())

    def test_header_sets(self):
        self.h.setBeginString("FIX.4.5")
        self.h.setBodyLength(63)
        self.h.setMsgType('5')
        self.h.setMsgSeqNum('3')
        self.h.setTargetCompId('FIXSIMA')
        self.h.setSendingTime("20180109-00:00:04.852")
        self.assertEqual("FIX.4.5", self.h.getBeginString())
        self.assertEqual(63, self.h.getBodyLength())
        self.assertEqual('5', self.h.getMsgType())
        self.assertEqual('3', self.h.getMsgSeqNum())
        self.assertEqual('FIXSIMA', self.h.getTargetCompId())
        self.assertEqual("20180109-00:00:04.852", self.h.getSendingTime())

    def test_trailer_gets(self):
        self.assertEqual('055', self.t.getCheckSum())

    def test_trailer_sets(self):
        self.t.setCheckSum('010')
        self.assertEqual('010', self.t.getCheckSum())

    def test_log_on_gets(self):
        self.assertEqual('30', self.log_on_msg.getHeartBeatInt())
        self.assertEqual(True, self.log_on_msg.getResetSeqNumFlag())

    def test_log_on_sets(self):
        self.log_on_msg.setHeartBeatInt('50')
        self.log_on_msg.setResetSeqNumFlag(False)
        self.assertEqual('50', self.log_on_msg.getHeartBeatInt())
        self.assertEqual(False, self.log_on_msg.getResetSeqNumFlag())
    
    def test_trade_message_gets(self):
        self.assertEqual("TEST1234", self.new_order_msg.getAccount())
        self.assertEqual('0', self.new_order_msg.getPrice())
        self.assertEqual(0, self.new_order_msg.getQuantity())
        self.assertEqual('buy', self.new_order_msg.getSide())
        self.assertEqual('\t0700', self.new_order_msg.getCode())
        self.assertEqual("20180109-07:01:01", self.new_order_msg.getTime())
        self.assertEqual('0', self.new_order_msg.getExecType())
        self.assertEqual("QO37NA54U3C8NTYKHDT15N4_0", self.new_order_msg.getOrderId())
        self.assertEqual('0', self.new_order_msg.getAverPrice())
        self.assertEqual(100, self.new_order_msg.getLeftQty())
        self.assertEqual(0, self.new_order_msg.getSumQty())


    def test_trade_message_sets(self):
        self.execu_order_msg.setAccount('TEST12345')
        self.execu_order_msg.setPrice('25')
        self.execu_order_msg.setQuantity(50)
        self.execu_order_msg.setSide('2')
        self.execu_order_msg.setCode(r'\t0922')
        self.execu_order_msg.setTime("20180109-07:01:03")
        self.execu_order_msg.setExecType('F')
        self.execu_order_msg.setOrderId("QO37NA54U3C8NTYKHDT15N5_0")
        self.execu_order_msg.setAverPrice('25')
        self.execu_order_msg.setLeftQty(50)
        self.execu_order_msg.setSumQty(50)
        self.assertEqual("TEST12345", self.execu_order_msg.getAccount())
        self.assertEqual('25', self.execu_order_msg.getPrice())
        self.assertEqual(50, self.execu_order_msg.getQuantity())
        self.assertEqual('sell', self.execu_order_msg.getSide())
        self.assertEqual(r'\t0922', self.execu_order_msg.getCode())
        self.assertEqual("20180109-07:01:03", self.execu_order_msg.getTime())
        self.assertEqual('F', self.execu_order_msg.getExecType())
        self.assertEqual("QO37NA54U3C8NTYKHDT15N5_0", self.execu_order_msg.getOrderId())
        self.assertEqual('25', self.execu_order_msg.getAverPrice())
        self.assertEqual(50, self.execu_order_msg.getLeftQty())
        self.assertEqual(50, self.execu_order_msg.getSumQty())
