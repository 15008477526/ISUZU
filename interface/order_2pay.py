from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class OederPay:

    @staticmethod
    def orderpay(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/pay"
        response = SendMethod.send_method(url=url, data=data)
        return response

    @staticmethod
    def get_succeed(data):
        """获取返回值中的succeed"""
        response = OederPay.orderpay(data)
        succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        return succeed


if __name__ == '__main__':
    from interface.login_interface import Login
    from interface.add_cart import Addcart

    login_data = {"name": "诸葛亮_1", "password": "Test123456"}
    session = Login.get_session(login_data)
    goods_id = Login.get_goods_id(login_data)
    addcart_data = {"session": session, "goods_id": goods_id, "number": 1}
    Addcart.addcart(addcart_data)

    orderpay_data = {"session": session, "order_id": 3987}
    print(OederPay.orderpay(orderpay_data))
