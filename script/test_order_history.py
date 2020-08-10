'''
@author:杨钟
@time:2019/09/22
'''
#历史订单
import unittest
from interface.login_3interface import Login
from interface.order_3history import History
from common.pymysql_e import Database
from common.get_keyword import GetKeyword

class TestHistoryPay(unittest.TestCase):
    def setUp(self):
        self.session = Login.get_session()
        self.db = Database()  # 实例化Database

    def test_history_pay(self):
        history_data =  {"session":self.session,"type":"finished","pagination":{"count":10,"page":1}}
        response=History.history(history_data)
        # print(response)
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
        # 判断待付款的订单是否在订单列表里
        self.assertIsNotNone(set(order).issubset(all_order))


if __name__ == '__main__':
    unittest.main()