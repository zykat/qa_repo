import unittest
import requests

TARGET_API = "https://breakingbadapi.com/api"
HTTP_OK = 200
TOTAL_CHARACTERS = 62
class TestMyAPI(unittest.TestCase):
    def test_fetch_all_characters(self):
        response = requests.get(f'{TARGET_API}characters')
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertEqual(len(response.json()), TOTAL_CHARACTERS,f'Failed: expecting fetch data about {TOTAL_CHARACTERS} characters!' )

if __name__=="__main__":
    unittest.main()