import unittest, os, sys
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

if __name__ == "__main__":

    test_dir = 'unit_test'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(discover)

    report_file = '../output/test_report.txt'
    with open(report_file, "w") as report_file:
        runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
        runner.run(discover)