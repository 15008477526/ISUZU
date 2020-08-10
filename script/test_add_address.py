'''
@author:魏江霖
@time:2019/9/23

测试添加收货地址
'''

import unittest
from interface.add_address_interface import Add_Address
from interface.login_interface import Login
from common.database import Database
from common.get_keyword import GetKeyword

class TestAddaddress(unittest.TestCase):
    '''测试收货地址'''
    def setUp(self):

        self.login_data = {'name': '123456', 'password': '123456'}
        self.session = Login.get_session(self.login_data)

    def test_add_address(self):
        add_data = {"address":{"default_address":0,"consignee":"小猪儿虫猪组长",
                               "tel":"12345969342","zipcode":"324535","country":"1",
                               "city":"118","id":0,"email":"123457@qq.com",
                               "address":"天府大道","province":"11",
                               "district":"1330","mobile":""},"session":self.session}

        Add_Address.add_address(add_data)
        consignee = GetKeyword.get_value_by_keyword(add_data,'consignee')
        db = Database()
        sql = 'select consignee from ecs_user_address where user_id=%s'
        login_response = Login.login(self.login_data)
        user_id = GetKeyword.get_value_by_keyword(login_response, 'id')
        args = user_id
        result = db.readall(sql,args)
        print(result) # [{'consignee': '马红梅'}, {'consignee': '猪儿虫'}, {'consignee': '小猪猪猪猪组长'}, {'consignee': '小猪儿虫猪组长'}]
        try:
            for i in result:
                # 遍历结果
                if consignee == i['consignee']:
                    self.assertTrue(consignee)
        except Exception as e:
            print(f'没有该用户的收货地址,{e}')

if __name__ == '__main__':
    unittest.main(verbosity=2)