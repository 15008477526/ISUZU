import unittest
from interface.login_interface import Login
from interface.cart_2list import CartList
from common.get_keyword import GetKeyword


class TestCartlist(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_cart_list(self):
        cart_list_data = {"session": self.session,"sid":"2daacb56c80866b512980baab9803b2c1bbaebce"}
        status_succeed = CartList.get_succeed(cart_list_data)
        self.assertEqual(status_succeed, 1)


if __name__ == '__main__':
    unittest.main()