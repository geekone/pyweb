import tempfile
import unittest



__author__ = 'Administrator'
import os

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
#        self.db_fd,app.config['DATABASE'] = tempfile.mkstemp()
        print tempfile.mkstemp()
        print "setup"


    def tearDown(self):
        print "tearDown"

    def test_empty_db(self):
        pass

if __name__ == '__main__':
    unittest.main()