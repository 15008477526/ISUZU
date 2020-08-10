'''
@author:周青松
@time:2019/9/22
'''

from common.send_method import SendMethod
from common.get_keyword import GetKeyword

# 收货地址管理
class RAM:
    @staticmethod
    def ram(data):
        # 请求地址
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/address/list'
        response = SendMethod.send_method(url=url,data=data)
        return response
    def get_session(data):
        """获取登录后的session"""
        response = Login.login(data)
        session = GetKeyword.get_value_by_keyword(response,"session")
        return session

    # 获取收货地址id
    @staticmethod
    def get_address_id(data):
        response = RAM.ram(data)
        address_id = GetKeyword.get_value_by_keyword(response, 'id')
        return address_id

    # 获取所有收货地址id
    @staticmethod
    def get_address_ids(data):
        response = RAM.ram(data)
        address_ids = GetKeyword.get_values_by_keyword(response, 'id')
        return address_ids


if __name__ == '__main__':
    from interface.login_interface import Login
    login_data = {'name':'zqs','password':'zqs950927'}
    # 获取登陆后的session
    session = Login.get_session(login_data)

    ram_data = {
        'session':session
    }
    RAM.ram(ram_data)
    print(RAM.ram(ram_data))
