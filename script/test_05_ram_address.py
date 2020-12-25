'''
@author:周青松
@time:2019/9/22
'''

import unittest
from interface.ram_5interface import RAM
class TestRamAddress(unittest.TestCase):
    '''测试收货地址列表'''
    def setUp(self):
        from common.pymysql_2222222 import Database
        # 调用database类操作mysql
        self.db = Database()
    def test_list_address(self):
        '''测试地址列表 '''

        sql = "select address_id from ecs_user_address where user_id=4335"
        try:
            address_ids = self.db.read_all(sql)
            for address_id in address_ids:

                # 查找数据库中的address_id
                address_id = address_id["address_id"]
                # 查找返回值中的ids
                ids = RAM.get_address_ids(sql)
                for id in ids:
                    # 断言
                    self.assertEqual(address_id, id)
        except Exception as e:
            print(e)



if __name__ == '__main__':
    unittest.main()