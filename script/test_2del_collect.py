import unittest
from interface.login_interface import Login
from interface.delete_2collect import DelCollect
from common.get_keyword import GetKeyword


class TestCollectGoods(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_delcollect(self):
        """测试删除收藏商品"""
        delcollect_data = {"session": self.session, "rec_id": "2225"}
        status_succeed = DelCollect.get_succeed(delcollect_data)
        self.assertEqual(status_succeed, 1)

if __name__ == '__main__':
    unittest.main()
