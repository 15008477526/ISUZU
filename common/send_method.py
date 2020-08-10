# 导入
import requests
import json

class SendMethod:

    # @staticmethod # 静态方法不需要使用实例化
    # def send_method(method, url, params=None, data=None):
    #     if method == 'get' or method == 'delete':
    #         response = requests.request(method=method, url=url, params=params)
    #     elif method == 'put' or method == 'post':
    #         response = requests.request(method=method, url=url, json=data)
    #
    #     else:
    #         print('请求方式有误!')
    #         response = None
    #     if method == 'delete':
    #         return response.status_code  # 如果请求方式是delete  返回状态码
    #     else:
    #         return response.json()


    @staticmethod
    def send_method(url, data):
        # 处理请求参数  请求参数:{"json":值}
        request_data = {"json": json.dumps(data)}
        # 请求参数类型:x-www-form-urlencoded
        response = requests.post(url=url, data=request_data)
        # 由于接口返回值类型为json格式
        return response.json()






if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/api/departments/'
    method = 'get'
    params = '$dep_id_list=11,12,13'
    print(SendMethod.send_method(method=method, url=url,params=params))