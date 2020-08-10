import unittest
from interface.login_interface import Login
from interface.order_2cancel_list import OrderCancelList
from common.get_keyword import GetKeyword
from interface.add_2cart import Addcart


class TestOrderCancelList(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_order_cancel_list(self):
        # addcart_data = {"session": self.session, "goods_id": 85, "number": 1}
        # Addcart.addcart(addcart_data)

        ordercancel_list_data = {"session":self.session,"type":"await_pay","pagination":{"count":10,"page":1}}
        status_succeed = OrderCancelList.get_succeed(ordercancel_list_data)
        self.assertEqual(status_succeed, 1)


if __name__ == '__main__':
    unittest.main()