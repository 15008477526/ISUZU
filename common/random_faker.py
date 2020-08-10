'''

'''
from faker import Faker
# 随机生成数据
def randomData():
    f=Faker(locale="zh_CN")
        #         名字      密码     地址         邮箱        手机             邮编
    return [f.name(),f.password(),f.address(), f.email(), f.phone_number(), f.postcode()]