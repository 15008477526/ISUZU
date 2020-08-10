from common.send_method import SendMethod

class Goods:
    @staticmethod
    def goods(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"
        response = SendMethod.send_method(url=url, data=data)
        return response


if __name__ == '__main__':
    from interface.login_interface import Login
    login_data = {"name":"leiyu","password":"leiyu980920"}
    session = Login.get_session(login_data)
    goods_data = {
     "goods_id": 85,
     "session": session
}
    print(Goods.goods(goods_data))