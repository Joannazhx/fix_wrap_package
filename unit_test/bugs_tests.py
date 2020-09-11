import os, sys
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)
from src.wrapper import *
import unittest
import re

class TestBugs(unittest.TestCase):
    """test test1.txt test2.txt compare results"""

    @classmethod
    def setUpClass(cls):
        print("test unknown bugs start :")
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        cls.file_path = os.path.abspath(os.path.join(path, 'input/FIX.09-Jan-2018.log'))
        cls.out_dir = os.path.abspath(os.path.join(path, 'unit_test/output/'))
        cls.wrap = Wrapper(cls.file_path, cls.out_dir)
        cls.read = Reader(cls.file_path)
        cls.lines = cls.read.read_log()

    @classmethod
    def tearDownClass(cls):
        print("test unknown bugs finished\n")
    
    def setUp(self):
        self.lines = self.read.read_log()

    def test_fix_format(self):
        for line in self.lines:
            messages = (line.split("|\n")[0]).split("|")
            self.assertEqual(messages[0], '8=FIX.4.4')
    
    def test_length(self):
        for line in self.lines:
            mess = self.read.read_line(line)
            line = re.sub("^(.*)\|9=(.*?)\|", r"", line)
            line = re.sub("\|10=(.*?)\|$", "|", line)
            print(line)
            self.assertEqual(mess.get_header().get_body_length(), len(line))

    def test_check_sum(self):
        for line in self.lines:
            mess = self.read.read_line(line)
            line = re.sub("\|10=(.*?)\|$", "|", line)
            print(line)
            # self.assertEqual(int(mess.get_trailer().get_check_sum()), len(line) % 256)
            self.assertEqual(int(mess.get_trailer().get_check_sum()), sys.getsizeof(line) % 256)

    def test_trade_qtys(self):
        for line in self.lines:
            if line[0] == '#':
                continue
            mess = self.read.read_line(line)
            order = self.wrap.update_order()
            if order is not None:
                if mess.get_exec_type() == '0':
                    self.wrap.get_order_pool().add_order(order)
                elif mess.get_exec_type() == 'F':
                    order_last = self.wrap.get_order_pool().serach_order(order.get_order_id())
                    self.assertEqual(order_last.get_cum_qty() + order.get_qty(), order.get_cum_qty())
                    self.assertEqual(order_last.get_cum_qty() + order_last.get_left_qty(), 
                                    order.get_cum_qty() + order.get_left_qty())

    def test_trade_price(self):
        for line in self.lines:
            if line[0] == '#':
                continue
            mess = self.read.read_line(line)
            order = self.wrap.update_order()
            if order is not None:
                if mess.get_exec_type() == '0':
                    self.wrap.get_order_pool().add_order(order)
                elif mess.get_exec_type() == 'F':
                    order_last = self.wrap.get_order_pool().serach_order(order.get_order_id())
                    last_price_total = order_last.get_cum_qty() *  float(order_last.get_aver_price())
                    cur_price_total = order_last.get_qty() *  float(order_last.get_price())
                    aver_cal = (last_price_total + cur_price_total) / order.get_cum_qty()
                    self.assertEqual(float(order.get_aver_price()), float(aver_cal))

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    test_dir = os.path.abspath(os.path.join(path, 'unit_test'))
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='bugs_tests.py')

    report_file = os.path.abspath(os.path.join(path, 'output/bugs_report.txt'))
    with open(report_file, "w") as report_file:
        runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
        runner.run(discover)

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(discover)