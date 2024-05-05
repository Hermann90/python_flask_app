import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_greet(self):
        response = self.app.get('/greet/John')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, John! Welcome to the Exciting Flask App.')

    def test_quote(self):
        response = self.app.get('/quote')
        self.assertEqual(response.status_code, 200)

    def test_random_number(self):
        response = self.app.get('/random')
        self.assertEqual(response.status_code, 200)
        # Check if the response is an integer
        try:
            int(response.data.decode('utf-8'))
        except ValueError:
            self.fail("Response is not an integer.")

if __name__ == '__main__':
    unittest.main()
