import unittest
import xmlrunner

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    discovery = unittest.TestLoader().discover('server/', pattern='*.py')
    runner.run(discovery)