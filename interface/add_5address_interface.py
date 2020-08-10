'''
@author:周青松
@time:2019/9/22
'''
from common.send_method import SendMethod
from common.get_keyword import GetKeyword

# 添加收货地址
class AddAddress:
    @staticmethod
    def add_address(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/address/add'
        response = SendMethod.send_method(url=url,data=data)
        return response



if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {'name': 'zqs', 'password': 'zqs950927'}
    # 获取登陆后的session
    session = Login.get_session(login_data)

    add_data = {"address":{"default_address":0,
                            "consignee":"艾希","tel":"123456",
                            "zipcode":"000000","country":"1","city":"102",
                            "id":0,"email":"zqs@qq.com","address":"000","province":"9",
                            "district":"1150","mobile":""},
                            "session":session}

    print(AddAddress.add_address(add_data))
