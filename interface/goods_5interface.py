from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class Goods:
    @staticmethod
    def goods(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"
        response = SendMethod.send_method(url=url, data=data)
        return response


if __name__ == '__main__':
    from interface.login_interface import Login
    login_data = {"name":"诸葛亮_1","password":"Test123456"}
    session = Login.get_session(login_data)
    goods_data = {
     "goods_id": 51,
     "session": session
}
    print(Goods.goods(goods_data))