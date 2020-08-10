'''
@author:周青松
@time:2019/9/22
'''

import unittest
from interface.login_interface import Login
from interface.goods_interface import Goods
from common.get_keyword import GetKeyword


class TestGoods(unittest.TestCase):
    '''登陆'''
    def setUp(self):
        login_data = {"name": "zqs", "password": "zqs950927"}
        self.session = Login.get_session(login_data)

    def test_goods_info(self):
        """测试商品详情"""
        goods_data = {"goods_id": 51,"session": self.session}
        response = Goods.goods(goods_data)
        status_succeed = GetKeyword.get_value_by_keyword(response,"succeed")
        self.assertEqual(status_succeed,1)

if __name__ == '__main__':
    unittest.main()