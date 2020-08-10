import unittest
from interface.order_flow import OrderFlow
from interface.login_interface import Login
from interface.add_cart import Cart
from common.get_keyword import GetKeyword


class Test_order_flow(unittest.TestCase):
    def setUp(self):
        # login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        login_data = {"name": "123456", "password": "123456"}
        self.session = Login.get_session(login_data)
        add_cart_data = {
            "spec": [],
            "session": self.session,
            "goods_id": 87,
            "number": 1
        }
        Cart.add_cart(add_cart_data)

    def test_order_flow(self):
        # 1.检查订单
        check_order_data = {"session": self.session}
        # 2.获取shippingid和payid
        res = OrderFlow.get_shippingid_payid(check_order_data)
        print(res)
        # 3.确认订单并获取order_id
        done_order_data = {"shipping_id": res[0], "session": self.session, "pay_id": res[1]}
        order_id = OrderFlow.get_order_id(done_order_data)
        print(order_id)
        # 4.确认支付
        pay_order_data = {"session": self.session, "order_id": order_id}
        response = OrderFlow.pay_order(pay_order_data)
        print(response)
        succeed = GetKeyword.get_value_by_keyword(response,"succeed")
        self.assertEqual(succeed,1)

if __name__ == '__main__':
    unittest.main()