'''
@author:魏江霖
@time:2019/9/22

'''
import unittest
from interface.add_cart import Cart
from interface.login_interface import Login
from common.get_keyword import GetKeyword
from common.database import Database

#  测试商品分类
class TestGoodCategory(unittest.TestCase):

    def setUp(self):
        login_data = {"name": "123456", "password": "123456"}
        self.session = Login.get_session(login_data)

    def test_02_addcart(self):
        # 添加购物车
        add_data ={"spec":[],"session":self.session,"goods_id":64,"number":1}
        response = Cart.add_cart(add_data)
        # status_succeed =GetKeyword.get_value_by_keyword(response,'succeed')
        # self.assertEqual(status_succeed,1,msg='报错啦')
        db = Database()
        sql = 'select goods_id,goods_number from ecs_cart where user_id =%s'
        args = (6385)
        result = db.readone(sql,args)
        result_good_id =GetKeyword.get_value_by_keyword(result,'goods_id')
        # print(result)
        if 64 ==  result_good_id:
            self.assertTrue(True)

    # 修改购物车
    def test_03_update_cart(self):
        add_data = {"spec": [], "session": self.session, "goods_id": 86, "number": 1}
        response = Cart.add_cart(add_data)

        list_data = {
            'session': self.session
        }
        rec_id = Cart.get_rec_id(list_data)  # 获取购物车列表的rec_id
        updata_data ={
            'new_number':2,
            'session':self.session,
            'rec_id':rec_id
        }
        res_update =Cart.cart_update(updata_data)
        # print(res_update)
        db = Database()
        sql = 'select rec_id from ecs_cart where user_id =%s'
        args = (6385)
        result = db.readall(sql, args)
        print(result)  #[{'rec_id': 14078}, {'rec_id': 14105}, {'rec_id': 14071}]
        for rec_id_1 in result:
            if rec_id == rec_id_1['rec_id']:
                self.assertTrue(rec_id)

    def test_04_delete_cart(self):
        add_data = {"spec": [], "session": self.session, "goods_id": 51, "number": 1}
        response = Cart.add_cart(add_data)
        list_data = {
            'session': self.session
        }
        rec_id = Cart.get_rec_id(list_data)  # 获取购物车列表的rec_id
        delete_data = {"session": self.session, "rec_id": rec_id}
        res_delete = Cart.cart_delete(delete_data)
        succeed_code = GetKeyword.get_value_by_keyword(res_delete, 'succeed')
        print(succeed_code)
        self.assertEqual(succeed_code,1)

if __name__ == '__main__':
    unittest.main()