from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class OrderCancel:

    @staticmethod
    def ordercancel(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/cancel"
        response = SendMethod.send_method(url=url, data=data)
        return response

    @staticmethod
    def get_succeed(data):
        """获取返回值中的succeed"""
        response = OrderCancel.ordercancel(data)
        succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        return succeed


if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {"name": "诸葛亮_1", "password": "Test123456"}
    session = Login.get_session(login_data)

    ordercancel_data = {"session": session, "order_id": 3983}
    print(OrderCancel.ordercancel(ordercancel_data))
