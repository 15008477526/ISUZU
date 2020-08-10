'''
@author:周青松
@time:2019/9/22
'''

from common.send_method import SendMethod
from common.get_keyword import GetKeyword
# 修改收货地址
class ModifyAddress:
    @staticmethod
    def modify_address(data):
        # 请求地址
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/address/update'
        # 请求参数
        response = SendMethod.send_method(url=url,data=data)
        return response


if __name__ == '__main__':
    from interface.login_interface import Login
    from interface.ram_interface import RAM
    login_data = {'name': 'zqs', 'password': 'zqs950927'}
    # 获取登陆后的session
    session = Login.get_session(login_data)

    ram_data = {
        "address": {"default_address": 0, "consignee": "雷雨",
                     "tel": "123456", "zipcode": "000000", "country": "1",
                     "city": "131", "id": 0, "email": "leiyu@qq.com",
                     "address": "召唤师西峡谷", "province": "12",
                     "district": "1440", "mobile": ""}, "address_id": "4292",
                     "session": session}

    # 获取地址id
    address_id = RAM.get_address_id(ram_data)
    # print(address_id)
    modify_data = {"address_id":address_id,"session":session}

    print(ModifyAddress.modify_address(modify_data))