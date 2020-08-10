from common.send_method import SendMethod
from common.get_keyword import GetKeyword

class Login:
    # 测试单接口
    @staticmethod
    def login():
        # 请求地址
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        # 请求参数
        response = SendMethod.send_method(url=url,data={"name":"ytks","password":"123456"})
        return response
    # 获取返回值中的具体字段,用于关联接口的数据传递
    @staticmethod
    def get_session():
        """获取登录后的session"""
        response = Login.login()
        session = GetKeyword.get_value_by_keyword(response,"session")
        return session
if __name__ == '__main__':
    print(Login.login())