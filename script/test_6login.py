import unittest
from interface.login_interface import Login
from common.get_keyword import GetKeyword
class TestLogin(unittest.TestCase):
    def test_lgoin(self):
        lgion_data = {"name": "ZXJ", "password": "123456"}
        response = Login.login(lgion_data)
        status_succeed = GetKeyword.get_value_by_keyword(response,"succeed")
        self.assertEqual(status_succeed,1)
if __name__ == '__main__':
    unittest.main()
