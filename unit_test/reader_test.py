from src.reader import *
import unittest

class TestReader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nReader class test start :")

    def setUp(self):
        self.reader = Reader("")
        pass
    
    @classmethod
    def tearDownClass(cls):
        print("Reader class test finished\n")

    def test_reader_create_mess_heart(self):
        mess_heart = {'8': 'FIX.4.4', '9': '58', '35': '0', '34': '1437', '49': 'FIXSIM', '52': '20180109-16:36:34.112', '56': 'QFSAMPLE', '10': '223'}
        mes = self.reader.createMessage(mess_heart)
        self.assertEqual('Message', type(mes).__name__)

        self.assertEqual("FIX.4.4", mes.getHeader().getBeginString())
        self.assertEqual(58, mes.getHeader().getBodyLength())
        self.assertEqual('0', mes.getHeader().getMsgType())
        self.assertEqual('1437', mes.getHeader().getMsgSeqNum())
        self.assertEqual('FIXSIM', mes.getHeader().getTargetCompId())
        self.assertEqual('20180109-16:36:34.112', mes.getHeader().getSendingTime())
        self.assertEqual('223', mes.getTrailer().getCheckSum())
    
    def test_reader_create_mess_logon(self):
        mes_log_on = {'8': 'FIX.4.4', '9': '73', '35': 'A', '34': '1', '49': 'FIXSIM', '52': '20180109-18:20:00.369', '56': 'QFSAMPLE', '98': '0', '108': '30', '141': 'Y', '10': '151'}
        mes = self.reader.createMessage(mes_log_on)
        self.assertEqual('LogOnMessage', type(mes).__name__)

        self.assertEqual('30', mes.getHeartBeatInt())
        self.assertEqual(True, mes.getResetSeqNumFlag())


    def test_reader_create_mess_trade(self):
        mes_trade = {'8': 'FIX.4.4', '9': '238', '35': '8', '34': '287', '49': 'FIXSIM', '52': '20180109-07:01:09.565', '56': 'QFSAMPLE', '1': 'TEST1234', '6': '25', '11': 'QO37NA54U3C8NU0LOVQ15N7_0', '14': '1000', '17': '47636510780695342000', '31': '25', '32': '1', '37': '47636510780695342000', '38': '1000', '39': '2', '54': '1', '55': '1357', '60': '20180109-07:01:09', '150': 'F', '151': '0', '207': 'HKE', '10': '099'}
        mes = self.reader.createMessage(mes_trade)
        self.assertEqual('TradeMessage', type(mes).__name__)

        self.assertEqual("TEST1234", mes.getAccount())
        self.assertEqual('25', mes.getPrice())
        self.assertEqual(1, mes.getQuantity())
        self.assertEqual('buy', mes.getSide())
        self.assertEqual('\t1357', mes.getCode())
        self.assertEqual("20180109-07:01:09", mes.getTime())
        self.assertEqual('F', mes.getExecType())
        self.assertEqual("QO37NA54U3C8NU0LOVQ15N7_0", mes.getOrderId())
        self.assertEqual('25', mes.getAverPrice())
        self.assertEqual(0, mes.getLeftQty())
        self.assertEqual(1000, mes.getSumQty())

    def test_reader_read_line(self):
        line = '8=FIX.4.4|9=238|35=8|34=287|49=FIXSIM|52=20180109-07:01:09.565|56=QFSAMPLE|1=TEST1234|6=25|11=QO37NA54U3C8NU0LOVQ15N7_0|14=1000|17=47636510780695342000|31=25|32=1|37=47636510780695342000|38=1000|39=2|54=1|55=1357|60=20180109-07:01:09|150=F|151=0|207=HKE|10=099|\n'
        mes = self.reader.read_line(line)

        self.assertEqual("FIX.4.4", mes.getHeader().getBeginString())
        self.assertEqual(238, mes.getHeader().getBodyLength())
        self.assertEqual('8', mes.getHeader().getMsgType())
        self.assertEqual('287', mes.getHeader().getMsgSeqNum())
        self.assertEqual('FIXSIM', mes.getHeader().getTargetCompId())
        self.assertEqual('20180109-07:01:09.565', mes.getHeader().getSendingTime())
        self.assertEqual('099', mes.getTrailer().getCheckSum())

        self.assertEqual("TEST1234", mes.getAccount())
        self.assertEqual('25', mes.getPrice())
        self.assertEqual(1, mes.getQuantity())
        self.assertEqual('buy', mes.getSide())
        self.assertEqual('\t1357', mes.getCode())
        self.assertEqual("20180109-07:01:09", mes.getTime())
        self.assertEqual('F', mes.getExecType())
        self.assertEqual("QO37NA54U3C8NU0LOVQ15N7_0", mes.getOrderId())
        self.assertEqual('25', mes.getAverPrice())
        self.assertEqual(0, mes.getLeftQty())
        self.assertEqual(1000, mes.getSumQty())
