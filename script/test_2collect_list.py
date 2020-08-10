import unittest
from interface.login_interface import Login
from interface.collect_2list import CollectList
from common.get_keyword import GetKeyword


class TestCollectList(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_collectlist(self):
        """测试查看收藏商品"""
        collectlist_data = {"session": self.session, "pagination": {"count": 10, "page": 1}, "rec_id": 0}
        status_succeed = CollectList.get_succeed(collectlist_data)
        self.assertEqual(status_succeed, 1)

if __name__ == '__main__':
    unittest.main()
