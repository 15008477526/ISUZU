import unittest
from interface.login_interface import Login
from interface.collect_2goods import CollectGoods
from common.get_keyword import GetKeyword


class TestCollectGoods(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_collectgoods(self):
        """测试收藏商品"""
        collectgoods_data = {"session": self.session, "goods_id": 32}
        status_succeed = CollectGoods.get_succeed(collectgoods_data)
        self.assertEqual(status_succeed, 1)


if __name__ == '__main__':
    unittest.main()
