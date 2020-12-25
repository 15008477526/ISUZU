
'''
创建对象后, 对象调用方法
'''

import pymysql
from common.config import config


class Database(object):
    def __init__(self):
        # 连接认证数据库,返回连接对象
        self.cnn = pymysql.connect(**config)



    def readone(self,query,args=None):
        '''
        读一条
        :param query要执行的sql语句
        :param args sql参数
        :return:
        '''
        # 连接对象创建游标
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.SSDictCursor)
        # sql语句传进来,args
        # 游标发送sql
        self.cursor.execute(query,args)
        # 游标获取结果
        result = self.cursor.fetchone()
        self.cursor.close()
        # 返回结果
        return  result

    def readall(self,query,args=None):
        '''
        读取所有
        :param query要执行的sql语句
        :param args sql参数
        :return:
        '''
        # 连接对象创建游标
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.SSDictCursor)
        # sql语句传进来,args
        # 游标发送sql
        self.cursor.execute(query, args)
        # 游标获取结果
        result = self.cursor.fetchall()
        self.cursor.close()
        # 返回结果
        return result

    def write(self,query,args=None):
        '''
        写操作(update,delete,insert into)
        :return:
        '''
        try:
            # 游标发送sql
            num = self.cursor.execute(query,args)
            # num 受影响的行
            if num > 0:
                # 提交事务
                self.cnn.commit()
            else:
                # 失败回滚
                self.cnn.rollback()
        except Exception as e:
            # 捕获异常,回滚
            self.cnn.rollback()
            print('错误信息:',e)


    def __del__(self):
        '''销毁'''
        # 关闭游标 关闭连接

        self.cnn.close()


if __name__ == '__main__':
    db = Database()
    # 调用方法
    sql ='select * from tm_dealer where name like %s'
    args =('北京%',)
    result = db.readone(sql,args)
    print(result)

    # sql1 ='update lol1 set age=32 where name=%s'
    # args =('麦林炮手',)
    # db.write(sql1,args)

