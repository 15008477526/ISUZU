'''
@author:魏江霖
@time:2019/9/23

收藏编辑删除
'''
from common.send_method import SendMethod
from interface.add_cart import Cart
from interface.login_interface import Login

class DeleteCollect:

    @staticmethod
    def delete_collect(data):
        '''编辑收藏 移除'''

        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/delete'
        response = SendMethod.send_method(url=url,data=data)
        return response



if __name__ == '__main__':
    login_data = {"name": "123456", "password": "123456"}
    session = Login.get_session(login_data)

    create_data = {
        'spec': [],
        'session': session,
        'goods_id': 86,
        'number': 1
    }
    res = Cart.add_cart(create_data)
    list_data = {
        'session': session
    }
    rec_id = Cart.get_rec_id(list_data)  # 获取购物车列表的rec_id
    print(rec_id)
    data = {"session": session, "rec_id": rec_id}
    DeleteCollect.delete_collect(data)