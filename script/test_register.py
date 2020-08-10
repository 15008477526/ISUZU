'''
'''
import unittest
from interface.register_interface import Register
from common.random_faker import randomData
from common.database import Database
from common.get_keyword import GetKeyword
from common.operate_excel import OperationExcel
oper = OperationExcel('./data/register.xls')


class TestRegister(unittest.TestCase):

    def test_register(self):
        random_data =randomData()
        name =random_data[0]
        email = random_data[3]
        value = random_data[4]
        password =random_data[1]
        data ={"field":[{"id":5,"value":f"{value}"}],
               "email":f"{email}",
               "name":f"{name}",
               "password":f"{password}"}
        response = Register.register(data)
        user_id =GetKeyword.get_value_by_keyword(response,'id')
        print(user_id)
        db = Database()
        sql = 'select user_name from ecs_users where user_id=%s'
        args =user_id
        result =db.readone(sql,args)
        print(result) #{'user_name': '李红'}
        self.assertEqual(name,result['user_name'])
        oper.write_data([value,email,name,password])

if __name__ == '__main__':
    unittest.main()