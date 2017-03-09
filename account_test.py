import unittest
from account import Account

class TestAccountModel(unittest.TestCase):

    def test_get_json(self):
        account = Account(123,"test@test.com","1","2")
        json = account.get_json()
        
        expected = """{
    "access_token": "1",
    "email": "test@test.com",
    "id": 123,
    "refresh_token": "2"
}"""

        self.assertEqual(json,expected)


if __name__ == '__main__':
    unittest.main()
