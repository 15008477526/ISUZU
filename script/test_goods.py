# import unittest
# from interface.login_interface import Login
# from interface.goods_interface import Goods
# from common.get_keyword import GetKeyword
#
#
# class TestGoods(unittest.TestCase):
#     def setUp(self):
#         self.session = Login.get_session()
#         # login_data = {"name": "ytks", "password": "123456"}
#         # self.session = Login.get_session(login_data)
#
#     def test_goods_info(self):
#         goods_data = {"goods_id": 51,"session": self.session}
#         response = Goods.goods(goods_data)
#         status_succeed = GetKeyword.get_value_by_keyword(response,"succeed")
#         self.assertEqual(status_succeed,1)
#         print(response)
#
# if __name__ == '__main__':
#     unittest.main()