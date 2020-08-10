'''
@author:魏江霖
@time:2019/9/22

注册
'''

from common.send_method import SendMethod
from common.get_keyword import GetKeyword

class Register:

    @staticmethod
    def register(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signup'
        response = SendMethod.send_method(url=url,data=data)
        return response

    @staticmethod
    def get_session(data):
        """获取注册后的session"""
        response = Register.register(data)
        session = GetKeyword.get_value_by_keyword(response, "session")
        return session


if __name__ == '__main__':
    data ={"field":[{"id":5,"value":"1234156"}],"email":"wjl123@qq.com","name":"wjl123","password":"123456"}
    print(Register.register(data))