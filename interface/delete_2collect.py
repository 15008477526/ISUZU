from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class DelCollect:
    @staticmethod
    def delcollect(data):
        # 请求地址
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/delete"
        # 请求参数
        response = SendMethod.send_method(url=url, data=data)
        return response

    # 获取返回值中的具体字段,用于关联接口的数据传递
    @staticmethod
    def get_succeed(data):
        """获取收藏返回值中的succeed"""
        response = DelCollect.delcollect(data)
        succeed = GetKeyword.get_value_by_keyword(response, "succeed")
        return succeed


if __name__ == '__main__':
    from interface.login_interface import Login

    login_data = {"name": "诸葛亮_1", "password": "Test123456"}
    session = Login.get_session(login_data)
    delcollect_data = {"session": session, "rec_id": "2235"}
    print(DelCollect.delcollect(delcollect_data))
