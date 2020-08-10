import unittest
from interface.login_interface import Login
from interface.order_2done import OrderDone
from common.get_keyword import GetKeyword
from interface.add_2cart import Addcart


class TestOrderDone(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_order_done(self):
        addcart_data = {"session": self.session, "goods_id": 85, "number": 1}
        Addcart.addcart(addcart_data)

        orderdone_data = {"shipping_id": "6", "session": self.session, "pay_id": "4"}
        status_succeed = OrderDone.get_succeed(orderdone_data)
        self.assertEqual(status_succeed, 1)


if __name__ == '__main__':
    unittest.main()