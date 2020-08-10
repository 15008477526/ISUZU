'''
@author:周青松
@time:2019/9/22
'''

from common.send_method import SendMethod
# 删除地址
class DeleteAddress:
    @staticmethod
    def delete_address(data):
        # 请求地址
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/address/delete'
        # 请求参数
        response = SendMethod.send_method(url=url, data=data)
        return response

if __name__ == '__main__':
    from interface.login_interface import Login
    from interface.ram_interface import RAM
    login_data = {'name': 'zqs', 'password': 'zqs950927'}
    # 获取登陆后的session
    session = Login.get_session(login_data)
    ram_data = {
        'session': session
    }
    # 获取地址id
    address_id = RAM.get_address_id(ram_data)
    delete_data = {'address_id':address_id,'session':session}

    print(DeleteAddress.delete_address(delete_data))