import os, sys, csv
import subprocess
import pandas as pd, numpy as np
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)
from src.wrapper import *
import unittest

class TestLogs(unittest.TestCase):
    """test test1.txt test2.txt compare results"""

    @classmethod
    def setUpClass(cls):
        print("test logs start :")

    @classmethod
    def tearDownClass(cls):
        print("test logs finished\n")


    def test_log1(self):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        sys.path.append(path)
        prc = subprocess.Popen("python src/main.py  -f unit_test/test_logs/test1.txt -o unit_test/test_logs/output1", shell=True)
        prc.wait()
        path1 = "unit_test/test_logs/output_1"
        path2 = "unit_test/test_logs/output1"
        results = self.csvs_compare(path1, path2)
        for re in results:
            self.assertEqual(True, re) 


    def test_log2(self):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        sys.path.append(path)
        if not os.path.isdir("unit_test/test_logs/output2"):
            os.mkdir("unit_test/test_logs/output2")
        prc = subprocess.Popen("python src/main.py  -f unit_test/test_logs/test2.txt -o unit_test/test_logs/output2", shell=True)
        prc.wait()
        path1 = "unit_test/test_logs/output_2"
        path2 = "unit_test/test_logs/output2"
        results = self.csvs_compare(path1, path2)
        for re in results:
            self.assertEqual(True, re)

    def read_csv(self, path, csv_file):
        file_p = os.path.abspath(os.path.join(os.path.abspath(path), csv_file))
        df = pd.read_csv(file_p)
        return df

    def csvs_compare(self, path1, path2):
        files = os.listdir(path1)
        results = []
        for csv_file in files:
            df1 = self.read_csv(path1, csv_file)
            df2 = self.read_csv(path2, csv_file)
            results.append((df1==df2).all().all())
        return results
            

            