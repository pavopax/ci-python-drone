import os
import picr
import unittest
import tempfile

class PicrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, picr.app.config['DATABASE'] = tempfile.mkstemp()
        picr.app.config['TESTING'] = True
        self.app = picr.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(picr.app.config['DATABASE'])

    # sample test that passes
    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'Upload new File' in rv.data


if __name__ == '__main__':
    unittest.main()
