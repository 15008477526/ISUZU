'''
@author:周青松
@time:2019/9/22
'''
import unittest
from interface.login_interface import Login
from common.get_keyword import GetKeyword
from interface.ram_5interface import RAM
from interface.delete_5ddress_interface import DeleteAddress

class TestDeleteAddress(unittest.TestCase):
    '''测试删除收货地址'''
    def setUp(self):
        # 登陆
        login_data = {'name': 'zqs', 'password': 'zqs950927'}
        # 获取登陆后的session
        self.session = Login.get_session(login_data)
        ram_data = {
            'session': self.session
        }
        # 获取收货地址id
        self.address_id = RAM.get_address_id(ram_data)

    def test_delete_address(self):
        delete_data = {'address_id':self.address_id,'session':self.session}
        response = DeleteAddress.delete_address(delete_data)
        status_succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        self.assertEqual(status_succeed, 1)

if __name__ == '__main__':
    unittest.main()