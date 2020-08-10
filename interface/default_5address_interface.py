'''
@author:周青松
@time:2019/9/22
'''

from common.send_method import SendMethod

# 设置默认地址
class DefaultAddress:
    @staticmethod
    def default_address(data):
        # 请求地址
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/address/setDefault'
        # 请求参数
        response = SendMethod.send_method(url=url,data=data)
        return response

if __name__ == '__main__':
    from interface.login_interface import Login
    from interface.ram_interface import RAM
    login_data = {'name': 'zqs', 'password': 'zqs950927'}
    # 获取登陆后的session
    session = Login.get_session(login_data)
    # 获取收货地址id
    ram_data = {
        'session': session
    }
    address_id = RAM.get_address_id(ram_data)
    # 请求参数
    default_data = {'address_id':address_id,'session':session}
    print(DefaultAddress.default_address(default_data))
