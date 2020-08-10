#历史订单
from common.send_method import SendMethod
from interface.login_3interface import Login
from common.get_keyword import GetKeyword
class History:
    Login.login()
    @staticmethod
    def history(data):
        url="http://ecshop.itsoso.cn/ECMobile/?url=/order/list"#请求地址
        response=SendMethod.send_method(url=url,data=data)
        return response
    @staticmethod
    def get_succeed(data):
        response = History.history(data)
        return GetKeyword.get_value_by_keyword(response,"succeed")

if __name__ == '__main__':
    from interface.login_interface import Login
    session = Login.get_session()
    print(session)

    data = {"session": session, "type": "finished", "pagination": {"count": 10, "page": 1}}
    print(History.history(data))
    print(History.get_succeed(data))