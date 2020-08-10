from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class Addcart:

    @staticmethod
    def addcart(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
        response = SendMethod.send_method(url=url, data=data)
        return response

    @staticmethod
    def get_succeed(data):
        """获取返回值中的succeed"""
        response = Addcart.addcart(data)
        succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        return succeed


if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {"name": "诸葛亮_1", "password": "Test123456"}
    session = Login.get_session(login_data)

    addcart_data = {"session": session, "goods_id": 85, "number": 1}
    print(Addcart.addcart(addcart_data))
