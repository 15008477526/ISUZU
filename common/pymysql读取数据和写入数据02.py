import pymysql

# 连接认证数据库
config ={
    'host':'.cn',
    'port':3306,
    'user':'',
    'password':'',
    'database':'',
    'charset':'utf8'
}

# 返回连接对象
cnn = pymysql.connect(**config)
# print(cnn)

# 连接对象创建游标对象
cursor = cnn.cursor(cursor=pymysql.cursors.SSDictCursor)


id = 1
config_id =2
file ='lol'
try:
    # 准备一条sql
    sql = 'insert into ecs_cert values (%s,%s,%s) '
    args =(id,config_id,file)

    num = cursor.execute(sql,args)
    print(num)
    if num > 0:
        # 提交事务,修改成功
        cnn.commit()
    else:
        # 失败回滚
        cnn.rollback()
except Exception as e:
    cnn.rollback()
    print('做错了:',e)


cursor.close()
cnn.close()


