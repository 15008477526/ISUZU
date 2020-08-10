'''
@author:魏江霖
@time:2019/9/23

收藏
'''

from common.send_method import SendMethod
from common.get_keyword import GetKeyword

class CollectGoods:
    '''收藏'''
    @staticmethod
    def collect_good(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/create'
        response = SendMethod.send_method(url=url,data=data)
        return response




if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {"name": "123456", "password": "123456"}
    session = Login.get_session(login_data)
    data =  {"session":session,"goods_id":86}
    response = CollectGoods.collect_good(data)
    print(response)  # {'data': [], 'status': {'succeed': 1}}

    # 再次收藏
    # {'status': {'succeed': 0, 'error_code': 10007, 'error_desc': '您已收藏过此商品'}}