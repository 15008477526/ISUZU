import unittest
from interface.login_interface import Login
from interface.order_2check import OederCheck
from common.get_keyword import GetKeyword
from interface.add_2cart import Addcart


class TestOrderCheck(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_order_check(self):
        addcart_data = {"session": self.session, "goods_id": 85, "number": 1}
        Addcart.addcart(addcart_data)
        order_check_data = {"session": self.session,"sid":"2daacb56c80866b512980baab9803b2c1bbaebce"}
        status_succeed = OederCheck.get_succeed(order_check_data)
        self.assertEqual(status_succeed, 1)


if __name__ == '__main__':
    unittest.main()