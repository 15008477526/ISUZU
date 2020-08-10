'''
商品种类
'''

from common.send_method import SendMethod

class GoodsCategory:

    @staticmethod
    def goods_category(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/goods'
        response =SendMethod.send_method(url=url,data=data)
        return response


if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {'name': '123456', 'password': '123456'}
    session = Login.get_session(login_data)

    data ={"goods_id":51,"session":session}
    print(GoodsCategory.goods_category(data))