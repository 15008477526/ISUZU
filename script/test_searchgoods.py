'''
@author:魏江霖
@time:2019/9/22

'''

from interface.search_good import SearchGoods
from common.get_keyword import GetKeyword
import unittest

class TestSearchGoods(unittest.TestCase):

    def test_01_search_goods(self):
        data = {"pagination":{"count":6,"page":1},"filter":{"keywords":"","sort_by":"price_asc","brand_id":"","category_id":"25","price_range":{"price_min":0,"price_max":0}}}
        response = SearchGoods.search_goods(data)
        succeed = GetKeyword.get_value_by_keyword(response,'succeed')
        self.assertEqual(succeed,1,msg='报错啦')


if __name__ == '__main__':
    unittest.main()