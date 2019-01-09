import unittest
from safu.app import create_app

app = create_app(config_object='tests.settings')


class HomeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
      self.client = app.test_client()

    def test_home_get(self):
      resp = self.client.get('/')
      self.assertEqual(200, resp.status_code)

    def test_home_empty_address(self):
      resp = self.client.post('/')
      self.assertEqual(400, resp.status_code)


class SubmitTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
      self.client = app.test_client()

    def test_submit_get(self):
        resp = self.client.get('/submit')
        self.assertEqual(200, resp.status_code)
    
    def test_submit_post(self):
      resp = self.client.post('/submit', data=dict(
          category="address11"
      ))
      self.assertEqual(200, resp.status_code)
    
    def test_submit_empty_query(self):
      resp = self.client.post('/submit')
      self.assertEqual(400, resp.status_code)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)