import unittest
import requests


class FlaskTestCase(unittest.TestCase):

    # Haha
    def test_index(self):
        response = requests.get("https://google.com")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()