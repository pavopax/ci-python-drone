import os
import io
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
    def test_root(self):
        rv = self.app.get('/')
        assert 'Upload new File' in rv.data

    def test_upload(self):
        data = dict(file=(io.BytesIO(b"xkcd"), 'test.jpg'))
        rv = self.app.post('/', data=data, follow_redirects=True)
        assert 'Upload new File' not in rv.data
        assert b"xkcd" in rv.data


if __name__ == '__main__':
    unittest.main()
