'''
添加购物车
'''
from common.send_method import SendMethod
from common.get_keyword import GetKeyword

class Cart:
    ''''''

    @staticmethod
    def add_cart(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/cart/create'
        response = SendMethod.send_method(url=url,data=data)
        return response

    @staticmethod
    def cart_list(data):
        # 购物车列表
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/cart/list'
        response = SendMethod.send_method(url=url, data=data)
        return response

    @staticmethod
    def get_rec_id(data):
        # 购物车列表获取rec_id
        response = Cart.cart_list(data)
        rec_id =GetKeyword.get_value_by_keyword(response,'rec_id')
        return rec_id

    @staticmethod
    def cart_update(data):
        # 修改购物车
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/cart/update'
        response = SendMethod.send_method(url=url,data=data)
        return response

    @staticmethod
    def cart_delete(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/cart/delete'
        response = SendMethod.send_method(url=url, data=data)
        return response


if __name__ == '__main__':
    from interface.login_interface import Login
    login_data={'name':'123456','password':'123456'}
    session = Login.get_session(login_data)
    create_data={
        'spec':[],
        'session':session,
        'goods_id':86,
        'number':1
    }
    res=Cart.add_cart(create_data)
    print(res)


    list_data={
        'session':session
    }
    rec_id =Cart.get_rec_id(list_data) #获取购物车列表的rec_id
    print(rec_id)
    # updata_data ={
    #     'new_number':2,
    #     'session':session,
    #     'rec_id':rec_id
    # }
    # res_update =AddCart.cart_update(updata_data)
    # print(res_update)

    delete_data ={"session":session,"rec_id":rec_id}
    res_delete = Cart.cart_delete(delete_data)
    succeed_code = GetKeyword.get_value_by_keyword(res_delete,'status')
    print(succeed_code)
