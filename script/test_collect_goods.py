'''
@author:魏江霖
@time:2019/9/23


'''
import unittest
from interface.collect_interface import CollectGoods
from interface.login_interface import Login

class TestCollect(unittest.TestCase):

    def setUp(self):

        login_data = {"name": "123456", "password": "123456"}
        self.session = Login.get_session(login_data)

    def test_collect_good(self):
        collect_data = {"session":self.session,"goods_id":85}
        response = CollectGoods.collect_good(collect_data)
        return response


if __name__ == '__main__':
    unittest.main()