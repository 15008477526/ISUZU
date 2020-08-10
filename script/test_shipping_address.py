'''
@author:魏江霖
@time:2019/9/23

测试收货地址
'''
import unittest
from interface.shipping_address_interface import ShippingAddress
from interface.login_interface import Login
from common.database import Database
from common.get_keyword import GetKeyword


class TestShippingAddress(unittest.TestCase):

    def setUp(self):
        self.login_data = {'name': '123456', 'password': '123456'}
        self.session = Login.get_session(self.login_data)

    def test_shipping_address(self):
        data = {"session": self.session}
        response = ShippingAddress.shipping_address(data)
        # print(response)
        id = GetKeyword.get_value_by_keyword(response,'id')
        # print(id)  # 4104
        db = Database()
        sql = 'select address_id from ecs_user_address where user_id = %s'
        login_response = Login.login(self.login_data)
        user_id = GetKeyword.get_value_by_keyword(login_response,'id')
        # print(user_id)  # 6385
        args =user_id
        result = db.readall(sql,args)
        print(result)  # [{'address_id': 4016}, {'address_id': 4104}]
        try:
            for add_id in result:
                if id == add_id['address_id']:
                    self.assertTrue(id)
        except Exception as e:
            print(f'没有该用户的收货地址,{e}')