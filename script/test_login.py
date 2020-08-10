'''
@author:魏江霖
@time:2019/9/22

'''

import unittest,ddt
from interface.login_interface import Login
from common.get_keyword import GetKeyword
from common.operate_excel import OperationExcel

oper = OperationExcel('./data/register.xls')
test_data = oper.get_data_by_index()

@ddt.ddt
class TestLogin(unittest.TestCase):
    '''测试登录'''

    @ddt.data(*test_data)
    def test_login(self,data):
        name = data['name']
        password=data['password']
        data = {"name":f"{name}","password":f"{password}"}
        response = Login.login(data)
        status_succeed = GetKeyword.get_value_by_keyword(response,'succeed')
        self.assertEqual(status_succeed,1)


if __name__ == '__main__':
    unittest.main()