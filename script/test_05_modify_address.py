'''
@author:周青松
@time:2019/9/22
'''
import unittest
from interface.login_interface import Login
from common.get_keyword import GetKeyword
from interface.modify_5address_interface import ModifyAddress

class TestModifyAddress(unittest.TestCase):
    '''测试修改收货地址'''
    def setUp(self):
        # 登陆
        login_data = {'name': 'zqs', 'password': 'zqs950927'}
        # 获取登陆后的session
        self.session = Login.get_session(login_data)

    def test_modify_address(self):
        modify_data = {"address":{"default_address":0,"consignee":"盖伦",
                                   "tel":"123456","zipcode":"00000011","country":"1",
                                   "city":"102","id":0,"email":"zqs@qq.com","address":"2222222",
                                   "province":"9","district":"1150","mobile":""},"address_id":"4120",
                                    "session":self.session}

        response = ModifyAddress.modify_address(modify_data)

        status_succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        self.assertEqual(status_succeed, 1)

if __name__ == '__main__':
    unittest.main()