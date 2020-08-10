'''
@author:周青松
@time:2019/9/22
'''


import unittest
from interface.login_interface import Login
from interface.add_5address_interface import AddAddress
from common.get_keyword import GetKeyword

class TestAddAddress(unittest.TestCase):
    '''测试添加收货地址'''
    def setUp(self):
        # 登陆
        login_data = {'name': 'zqs', 'password': 'zqs950927'}
        # 获取登陆后的session
        self.session = Login.get_session(login_data)

    def test_add_address(self):
        add_data = {"address":{"default_address":0,"consignee":"泰达米尔",
                                "tel":"123456","zipcode":"000000","country":"1",
                                "city":"40","id":0,"email":"zqs@qq.com","address":"111",
                                "province":"4","district":"469","mobile":""},
                                "session":self.session}
        response = AddAddress.add_address(add_data)
        status_succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        self.assertEqual(status_succeed, 1)

if __name__ == '__main__':
    unittest.main()