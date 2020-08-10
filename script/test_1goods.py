import unittest
from interface.login_interface import Login
from interface.goods_interface import Goods
from common.get_keyword import GetKeyword
import ddt
# from common.database2 import Database
#
# database = Database()
# sql = 'select goods_id from ecs_goods '
# goods_id = database.readall(sql)


goods_id=[85,8,73,35,162,37,39,32,92,87,40,61]
@ddt.ddt
class TestGoods(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "leiyu", "password": "leiyu980920"}  # 登录
        self.session = Login.get_session(login_data)

    @ddt.data(*goods_id)
    def test_goods_info(self,goods_id):

        """测试商品详情"""
        goods_data = {"goods_id":goods_id,"session": self.session}
        response = Goods.goods(goods_data)
        status_succeed = GetKeyword.get_value_by_keyword(response,"succeed")
        # 断言
        self.assertEqual(status_succeed,1)



if __name__ == '__main__':
    unittest.main()
