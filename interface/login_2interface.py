from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class Login:
    # 测试单接口
    @staticmethod
    def login(data):
        # 请求地址
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        # 请求参数
        response = SendMethod.send_method(url=url, data=data)
        return response

    # 获取返回值中的具体字段,用于关联接口的数据传递
    @staticmethod
    def get_session(data):
        """获取登录后的session"""
        response = Login.login(data)
        session = GetKeyword.get_value_by_keyword(response, "session")
        return session

    @staticmethod
    def get_goods_id(data):
        response = Login.login(data)
        goods_id = GetKeyword.get_values_by_keyword(response,"goods_id")
        return goods_id


if __name__ == '__main__':
    data = {"name": "诸葛亮_1", "password": "Test123456"}
    print(Login.login(data))
