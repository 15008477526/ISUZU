#待付款
import unittest
from interface.login_3interface import Login
from interface.wait_for_3receiving import Wait
from common.get_keyword import GetKeyword
from common.pymysql_e import Database

class TestWaitPay(unittest.TestCase):
    def setUp(self):
        self.session = Login.get_session()
        self.db = Database()


    def test_wait_pay(self):
        wait_data = {"goods_id": 3882, "session": self.session}
        response = Wait.wait(wait_data)
        # 获取返回值中的订单号
        order = GetKeyword.get_value_by_keyword(response, "order_sn")
        print(order)
        # 获取用户的uid
        uid = GetKeyword.get_value_by_keyword(self.session, 'uid')
        # print(type(uid))
        # 查找订单表中对应用户的所有的待付款订单号
        all_order_sn = self.db.read_all(f"select order_sn from ecs_order_info where user_id = {uid}")
        # print(all_order_sn)
        # 返回的order_sn是列表格式,获取所有的值
        all_order = GetKeyword.get_values_by_keyword(all_order_sn, "order_sn")
        print(all_order)
        # 判断待付款的订单是否在订单列表里面 子集
        self.assertIsNotNone(set(order).issubset(all_order))
if __name__ == '__main__':
    unittest.main()