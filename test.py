import unittest
import xmlrunner
import sys

if __name__ == '__main__':
    args = sys.argv
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    discovery = unittest.TestLoader().discover(args[1], pattern='*.py')
    runner.run(discovery)
