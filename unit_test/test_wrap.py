from message_test import *

if __name__ == "__main__":

    test_dir = '.'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(discover)

    # report_file = '../output/test_report.txt'
    # with open(report_file, "w") as report_file:
    #     runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
    #     runner.run(discover)