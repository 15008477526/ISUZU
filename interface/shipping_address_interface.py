'''
@author:魏江霖
@time:2019/9/23

收货地址
'''
from common.send_method import SendMethod

class ShippingAddress:
    '''收货地址'''
    @staticmethod
    def shipping_address(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/address/list'
        response = SendMethod.send_method(url=url,data=data)
        return response


if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {'name': '123456', 'password': '123456'}
    session = Login.get_session(login_data)

    data ={"session":session}
    response = ShippingAddress.shipping_address(data)
    print(response)