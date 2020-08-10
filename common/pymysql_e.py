import pymysql


class Database(object):
    def __init__(self, host='cn', port=3306, charset='utf8'):
        self.cnn = pymysql.connect(user='', password='', database='', host='.cn', port=3306,
                                   charset='utf8')
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.SSDictCursor)  # 创建游标

    def read_one(self, query, args=None):  # 不确定是否有参数,设置默认值None
        """
        读取一条记录
        :param query:sql语句
        :param args: sql语句的参数
        :return: 返回读取的记录
        """
        self.cursor.execute(query, args)  # 执行sql语句
        data = self.cursor.fetchone()  # 获取第一条记录将其返回
        # 如果用SS游标类型,因为其为生成器,所以只读取了一个,剩余的内容没有读完
        # 此时如果再执行其他方法,会提示warning: previous unbufferd result was lef incompleted
        # 所以要在执行完成后关闭游标
        # 需要关闭游标后再return,先return+中断方法执行,关闭游标操作无法执行
        self.cursor.close()
        return data

    def read_many(self, query, args=None):
        """
        读取多条记录
        """
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.SSDictCursor)  # 因为游标已经关闭,所以要重建
        self.cursor.execute(query, args)  # 执行sql语句
        data = self.cursor.fetchmany(4)  # 读取前4条记录并将其返回
        self.cursor.close()
        return data

    def read_all(self, query, args=None):
        """
        读取全部记录
        :param query:sql语句
        :param args: sql语句的参数
        :return: 返回读取的记录
        """
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.SSDictCursor)
        self.cursor.execute(query, args)
        data = self.cursor.fetchall()  # 读取全部记录并将其返回
        self.cursor.close()
        return data

    def write(self, query, args=None):  # 不确定是否有参数,设置默认值None
        # execute方法返回一个int型,就是mysql执行操作时'受影响的行',
        # 但是只有在执行insert,delete,update这三个操作时,返回的数字才和mysql中受影响行的数量一致,如果是查询的话并不为0
        # 所以只适用于写的操作中
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.SSDictCursor)
        try:  # 用try来防止代码错误中断程序执行
            num = self.cursor.execute(query, args)
            if num > 0:  # 做出判断,如果num>0,说明表的修改成功
                self.cnn.commit()  # 提交事务
                return True  # 返回一个True
            else:
                self.cnn.rollback()  # 回滚事务
                return False  # 返回一个False
        except Exception as e:
            self.cnn.rollback()
            return False
        finally:
            self.cursor.close()

    def write_many(self, query, args=None):
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.SSDictCursor)
        try:
            num = self.cursor.executemany(query, args)  # 执行多组数据的写的操作
            if num > 0:  # 做出判断,如果num>0,说明表的修改成功
                self.cnn.commit()  # 提交事务
                return True  # 返回一个True
            else:
                self.cnn.rollback()  # 回滚事务
                return False  # 返回一个False
        except Exception as e:
            self.cnn.rollback()
            return False
        finally:
            self.cursor.close()

    def __del__(self):  # 代码执行完毕,关闭游标,断开连接
        self.cnn.close()


if __name__ == '__main__':
    db = Database()
    # 读取一条记录方法
    # sql = 'select * from ecs_user_address'
    # data = db.read_one(sql)
    # print(data)

    # 读取多条记录方法
    sql = 'select * from ecs_user_address where user_id=6435'
    data = db.read_many(sql)
    print(data)

    # 读取全部记录
    # sql = 'select * from ecs_user_address'
    # data = db.read_all(sql)
    # print(data)

    # 写的操作
    # sql = 'update ecs_user_address set name = %s,age = %s where name = %s'
    # args = ('C罗', 31, '埃尔克森')
    # check = db.write(sql, args)
    # print(check)

    # # 写多个的操作
    # sql = 'update student set name = %s,age = %s where name = %s'
    # args = [('梅西', 31, '郝海东'), ('内马尔', 27, '武磊')]  # 多个数据用中括号框起来组成一个列表
    # check = db.write_many(sql, args)
    # print(check)
