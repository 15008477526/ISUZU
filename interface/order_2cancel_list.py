from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class OrderCancelList:

    @staticmethod
    def ordercancel_list(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/list"
        response = SendMethod.send_method(url=url, data=data)
        return response

    @staticmethod
    def get_succeed(data):
        """获取返回值中的succeed"""
        response = OrderCancelList.ordercancel_list(data)
        succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        return succeed


if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {"name": "诸葛亮_1", "password": "Test123456"}
    session = Login.get_session(login_data)
    ordercancel_list_data = {"session":session,"type":"await_pay","pagination":{"count":10,"page":1}}
    print(OrderCancelList.ordercancel_list(ordercancel_list_data))
