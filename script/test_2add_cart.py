import unittest
from interface.login_interface import Login
from interface.add_2cart import Addcart
from common.get_keyword import GetKeyword


class TestAddCart(unittest.TestCase):
    def setUp(self):
        login_data = {"name": "诸葛亮_1", "password": "Test123456"}
        self.session = Login.get_session(login_data)

    def test_addcart(self):
        """测试收藏商品"""
        addcart_data = {"session": self.session, "goods_id": 85,"number":1}
        status_succeed = Addcart.get_succeed(addcart_data)
        self.assertEqual(status_succeed, 1)


if __name__ == '__main__':
    unittest.main()
