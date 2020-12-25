'''
@author:魏江霖
@time:2019/9/22

'''
config ={
    'host':'192.168.201.52',
    'port':3306,
    'user':'root',
    'password':'1234qwer!',
    'database':'vehicle_domain',
    'charset':'utf8'
}


# import psycopg2
#
# def sql():
#     conn = psycopg2.connect(database='vehicle',user='postgres',password='123456',host='saic.che.link',port='4885')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM vehicle_car LIMIT 10")
#     rows = cur.fetchall()
#     print(rows)
#     conn.commit()
#     cur.close()
#
# if __name__ == '__main__':
#     sql()