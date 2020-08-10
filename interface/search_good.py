'''
搜索商品
'''
from common.send_method import SendMethod


class SearchGoods:

    @staticmethod
    def search_goods(data):
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/search'
        response = SendMethod.send_method(url=url,data=data)
        return response



if __name__ == '__main__':
    data = {"pagination":{"count":6,"page":1},"filter":{"keywords":"","sort_by":"price_asc","brand_id":"","category_id":"25","price_range":{"price_min":0,"price_max":0}}}
    print(SearchGoods.search_goods(data))

