from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class OrderFlow:
    @ staticmethod
    def chcek_order(data):
        # 检查订单
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/flow/checkOrder"
        response = SendMethod.send_method(url=url, data=data)
        return response

    @ staticmethod
    def get_shippingid_payid(data):
        # 获取shippingid和payid
        res = OrderFlow.chcek_order(data)
        shipping_id = GetKeyword.get_value_by_keyword(res,"shipping_id")
        pay_id = GetKeyword.get_value_by_keyword(res, "pay_id")
        return shipping_id,pay_id

    @ staticmethod
    def done_order(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/flow/done"
        response = SendMethod.send_method(url=url, data=data)
        return response

    @ staticmethod
    def get_order_id(data):
        response = OrderFlow.done_order(data)
        order_sn = GetKeyword.get_value_by_keyword(response,"order_id")
        return order_sn

    @staticmethod
    def pay_order(data):
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/pay"
        response = SendMethod.send_method(url=url, data=data)
        return response



if __name__ == '__main__':
    from interface.login_interface import Login
    from interface.add_cart import Cart
    login_data = {"name":"123456","password":"123456"}
    session = Login.get_session(login_data)
    add_cart_data = {
         "spec": [],
         "session": session,
         "goods_id": 61,
         "number": 1
        }
    Cart.add_cart(add_cart_data)
    check_order_data = {"session":session}
    res = OrderFlow.get_shippingid_payid(check_order_data)
    print(res)
    done_order_data = {"shipping_id":res[0],"session":session,"pay_id":res[1]}
    order_id = OrderFlow.get_order_id(done_order_data)
    print(order_id)
    pay_order_data = {"session":session, "order_id":order_id}
    response = OrderFlow.pay_order(pay_order_data)
    print(response)

