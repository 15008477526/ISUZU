#待收货
from common.send_method import SendMethod
from interface.login_3interface import Login
from common.get_keyword import GetKeyword
class Wait:
    Login.login()
    @staticmethod
    def wait(data):
        url="http://ecshop.itsoso.cn/ECMobile/?url=/order/list"
        response=SendMethod.send_method(url=url,data=data)
        return response
    @staticmethod
    def get_succeed(data):
        response = Wait.wait(data)
        return GetKeyword.get_value_by_keyword(response,"succeed")
if __name__ == '__main__':
    from interface.login_interface import Login
    session=Login.get_session()
    print(session)
    data={"session":session,"type":"shipped","pagination":{"count":10,"page":1}}
    print(Wait.get_succeed(data))
