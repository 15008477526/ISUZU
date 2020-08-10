import unittest
from interface.login_interface import Login
from interface.order_2cancel import OrderCancel
from common.get_keyword import GetKeyword
from interface.add_2cart import Addcart


class TestOrderCancel(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_order_cancel(self):
        ordercancel_data = {"session": self.session, "order_id": 3991}
        status_succeed = OrderCancel.get_succeed(ordercancel_data)
        self.assertEqual(status_succeed, 1)


if __name__ == '__main__':
    unittest.main()
