'''
@author:杨钟
@time:2019/09/22
'''
from common.pymysql_e import Database
import unittest
from interface.login_3interface import Login
from interface.pending import Pending
from common.get_keyword import GetKeyword

# 创建测试类-待付款订单
class TestPendPay(unittest.TestCase):
    def setUp(self):
        # 获取登陆后的session
        self.session = Login.get_session()
        self.db = Database()#实例化

    def test_pend_pay(self):
        # 设置请求参数
        pend_data ={"session":self.session,"type":"await_pay","pagination":{"count":10,"page":1}}
        # 获取待付款订单返回值
        response=Pending.pending(pend_data)
        # print(response)
        # 获取返回值中的订单号
        order=GetKeyword.get_value_by_keyword(response,"order_sn")
        print(order)
        # 获取用户的uid
        uid=GetKeyword.get_value_by_keyword(self.session,'uid')
        # print(type(uid))
        # 查找订单表中对应用户的所有的待付款订单号
        all_order_sn=self.db.read_all(f"select order_sn from ecs_order_info where user_id = {uid}")
        # print(all_order_sn)
        # 返回的order_sn是列表格式,获取所有的值
        all_order = GetKeyword.get_values_by_keyword(all_order_sn,"order_sn")
        print(all_order)
        # 判断待付款的订单是否在订单列表里面 子集
        self.assertIsNotNone(set(order).issubset(all_order))
if __name__ == '__main__':
    unittest.main()