from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class OederCheck:

    @staticmethod
    def ordercheck(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/flow/checkOrder"
        response = SendMethod.send_method(url=url, data=data)
        return response

    @staticmethod
    def get_succeed(data):
        """获取返回值中的succeed"""
        response = OederCheck.ordercheck(data)
        succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        return succeed


if __name__ == '__main__':
    from interface.login_interface import Login
    from interface.add_cart import Addcart

    login_data = {"name": "诸葛亮_1", "password": "Test123456"}
    session = Login.get_session(login_data)
    addcart_data = {"session": session, "goods_id": 85, "number": 1}
    Addcart.addcart(addcart_data)
    ordercheck_data = {"session": session, "sid": "2daacb56c80866b512980baab9803b2c1bbaebce"}
    print(OederCheck.ordercheck(ordercheck_data))
