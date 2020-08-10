'''
@author:魏江霖
@time:2019/9/23

添加收货地址
'''

from common.send_method import SendMethod


class Add_Address:
    '''添加收货地址'''
    @staticmethod
    def add_address(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/address/add'
        response = SendMethod.send_method(url=url,data=data)
        return response

if __name__ == '__main__':
    from interface.login_interface import Login
    login_data ={'name': '123456', 'password': '123456'}
    session = Login.get_session(login_data)

    add_data = {"address":{"default_address":0,"consignee":"小猪猪猪猪组长","tel":"12345969342","zipcode":"324535","country":"1","city":"118","id":0,"email":"123457@qq.com","address":"天府大道","province":"11","district":"1330","mobile":""},"session":session}
    response = Add_Address.add_address(add_data)
    print(response)  # {'data': [], 'status': {'succeed': 1}}