import os
import picr                     # my picr.py file
import unittest
import tempfile

class PicrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, picr.app.config['DATABASE'] = tempfile.mkstemp()
        picr.app.config['TESTING'] = True
        self.app = picr.app.test_client()
        picr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(picr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
