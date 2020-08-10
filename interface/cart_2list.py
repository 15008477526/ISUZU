from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class CartList:

    @staticmethod
    def cartlist(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/list"
        response = SendMethod.send_method(url=url, data=data)
        return response

    @staticmethod
    def get_succeed(data):
        """获取返回值中的succeed"""
        response = CartList.cartlist(data)
        succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        return succeed


if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {"name": "诸葛亮_1", "password": "Test123456"}
    session = Login.get_session(login_data)

    cartlist_data = {"session": session, "sid": "2daacb56c80866b512980baab9803b2c1bbaebce"}
    print(CartList.cartlist(cartlist_data))
