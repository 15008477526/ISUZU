import time
import binascii
import logging
from socket import *
from isuzu import get_location,db_Connection
import random

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def x_o_r(byte1, byte2):    #XOR异或运算
    return hex(byte1 ^ byte2)

class AinasciiA2bHex():
    """
        Customization http action word base requests lib
    """
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'

    def __init__(self):
        # self.vin = vin
        pass

    def terminal_vehicle_login(self,vin):
        '''发送车辆登录：请求参数：车辆vin码、gateway地址、gateway端口'''
        # 燃油车LETAEEG3XKH921003
        # binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000138393836303331393336323030393238323935360118535657503839383630333139343732303836363633343036BF'
        # 燃油车FH000033
        binascii_data = '232301FE4C4554454444453130454830303030303201001C1401150F282000013839383630393139373130303235303537383234B2'

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]

        if len(month) == 1:
            month = '0' + month
        day = hex(int(now_time[8:10]))[2:]
        if len(day) == 1:
            day = '0' + day
        hour = hex(int(now_time[11:13]))[2:]
        if len(hour) == 1:
            hour = '0' + hour
        minute = hex(int(now_time[14:16]))[2:]
        if len(minute) == 1:
            minute = '0' + minute
        second = hex(int(now_time[17:19]))[2:]
        if len(second) == 1:
            second = '0' + second
        now_time = (year + month + day + hour + minute + second).upper()
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()
        binascii_data = binascii_data.replace(binascii_data[8:42] ,b2a_hex_vin)  #替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60],now_time)  #替换时间
        data = binascii_data[:-2]
        byte1 = int(str(data[0:2]), 16)
        for i in range(len(data) - 2):
            i = i + 2
            if i % 2 == 0:
                byte2 = int(str(data[i:i + 2]), 16)
                byte1 = x_o_r(byte1, byte2)[2:]
                byte1 = int(str(byte1), 16)
        BCC =  (hex(byte1)[2:]).upper()
        if len(BCC) == 1:
            BCC = '0' + BCC
        binascii_data =data + BCC
        print(f'登录的报文是:{binascii_data}')
        senddata = binascii.a2b_hex(binascii_data.strip())
        return senddata

    def terminal_vehicle_upload_realtime(self,vin,Longitude,Latitude,mileage):
        '''发送燃油车车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''

        # binascii_data = '232302FE4C455445444445313045483030303030320100F41401150F28210001011401150F28210000002500C34C45544544444531304548303030303032544553545F56455253494F4E5F56312E303043564E5F56414C5545303030303030303030495550525F56414C554530303030303030303030303030303030303030303030303030300111111111021401150F2821330098968B056100BB287D29134700E64334435D007878BE000633F38E01D40678000007D0801401150F2821004C271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E958271904000000AB271A01033E8101343E820130C8'
        binascii_data = '232302FE4C455445444445313045483030303030320100F41401150F28210001011401150F28210000002500C34C45544544444531304548303030303032544553545F56455253494F4E5F56312E303043564E5F56414C5545303030303030303030495550525F56414C554530303030303030303030303030303030303030303030303030300111111111021401150F2821330098968B056100BB287D29134700E64334435D007878BE000633F38E01D40678000007D0801401150F2821004C271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E958271904001A20ED271A01033E8101343E820130B4'
        # binascii_data = '232302FE4C45544145454733584B483932313030330100E8140311120B2C0604010000000000000100000000004C45544145454733584B483932313030333030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030300002140311120B2C0000CB7D8300000000FFFFFFFF380000FFFFFFFF0000376F0006E5AF0101B4D304000043A880140311120B2C0044271102000427120100271302000027140F000000000000000000000000000000271506000000000000271602003727170102271804000043A82719040000128E271A010135'

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        speed = hex(random.randint(0, 999))[2:].upper()
        mileage = hex(mileage)[2:].upper()

        if len(mileage) != 8:
            m = (8 - len(mileage)) * str(0)
        mileage = m + mileage
        if len(speed) == 3:
            speed = "0" + speed
        if len(speed) == 2:
            speed = "00" + speed
        if len(speed) == 1:
            speed = "000" + speed
        if len(month) == 1:
            month = '0' + month
        day = hex(int(now_time[8:10]))[2:]
        if len(day) == 1:
            day = '0' + day
        hour = hex(int(now_time[11:13]))[2:]
        if len(hour) == 1:
            hour = '0' + hour
        minute = hex(int(now_time[14:16]))[2:]
        if len(minute) == 1:
            minute = '0' + minute
        second = hex(int(now_time[17:19]))[2:]
        if len(second) == 1:
            second = '0' + second
        now_time = (year + month + day + hour + minute + second).upper()  #当前时间转换成16进制
        # print(now_time)
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode() #VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[90:124], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换数据发送时间
        time.sleep(2)
        now_time_1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        year_1 = hex(int(now_time_1[2:4]))[2:]
        month_1 = hex(int(now_time_1[5:7]))[2:]
        if len(month_1) == 1:
            month_1 = '0' + month_1
        day_1 = hex(int(now_time_1[8:10]))[2:]
        if len(day_1) == 1:
            day_1 = '0' + day_1
        hour_1 = hex(int(now_time_1[11:13]))[2:]
        if len(hour_1) == 1:
            hour_1 = '0' + hour_1
        minute_1 = hex(int(now_time_1[14:16]))[2:]
        if len(minute_1) == 1:
            minute_1 = '0' + minute_1
        second_1 = hex(int(now_time_1[17:19]))[2:]
        if len(second_1) == 1:
            second_1 = '0' + second_1
        now_time_1 = (year_1 + month_1 + day_1 + hour_1 + minute_1 + second_1).upper()  # 当前时间转换成16进制
        binascii_data = binascii_data.replace(binascii_data[66:78], now_time_1)  # 替换信息采集时间
        binascii_data = binascii_data.replace(binascii_data[280:292], now_time_1)  # 替换信息采集时间
        binascii_data = binascii_data.replace(binascii_data[368:380], now_time_1)  # 替换信息采集时间
        # binascii_data = binascii_data.replace(binascii_data[90:124], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[342:350], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[350:358], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[358:366], mileage)  #替换里程
        data = binascii_data[:-2]
        byte1 = int(str(data[0:2]), 16)
        for i in range(len(data) - 2):   #XOR异或运算得出BCC
            i = i + 2
            if i % 2 == 0:
                byte2 = int(str(data[i:i + 2]), 16)
                byte1 = x_o_r(byte1, byte2)[2:]
                byte1 = int(str(byte1), 16)
        BCC =  (hex(byte1)[2:]).upper()
        if len(BCC) == 1:
            BCC = '0' + BCC
        binascii_data =data + BCC
        print(f'实时报文是:{binascii_data}')
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_upload_realtime_flameout(self,vin,Longitude,Latitude,mileage):
        '''发送车辆熄火数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        binascii_data = '232302FE4C455445444445313045483030303030320100F41401150F28210001011401150F28210000002500C34C45544544444531304548303030303032544553545F56455253494F4E5F56312E303043564E5F56414C5545303030303030303030495550525F56414C554530303030303030303030303030303030303030303030303030300111111111021401150F2821330098968B056100BB287D29134700E64334435D007878BE000633F38E01D40678000007D0801401150F2821004C271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701022718040000E958271904000000AB271A01033E8101343E820130CB'
        # binascii_data = '232302FE4C45544145454733584B483932313030330100E8140311120B2C0604010000000000000100000000004C45544145454733584B483932313030333030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030300002140311120B2C0000CB7D8300000000FFFFFFFF380000FFFFFFFF0000376F0006E5AF0101B4D304000043A880140311120B2C0044271102000427120100271302000027140F000000000000000000000000000000271506000000000000271602003727170102271804000043A82719040000128E271A010135'

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        speed = hex(random.randint(0, 999))[2:].upper()
        mileage = hex(mileage)[2:].upper()

        if len(mileage) != 8:
            m = (8 - len(mileage)) * str(0)
        mileage = m + mileage
        if len(speed) == 3:
            speed = "0" + speed
        if len(speed) == 2:
            speed = "00" + speed
        if len(speed) == 1:
            speed = "000" + speed
        if len(month) == 1:
            month = '0' + month
        day = hex(int(now_time[8:10]))[2:]
        if len(day) == 1:
            day = '0' + day
        hour = hex(int(now_time[11:13]))[2:]
        if len(hour) == 1:
            hour = '0' + hour
        minute = hex(int(now_time[14:16]))[2:]
        if len(minute) == 1:
            minute = '0' + minute
        second = hex(int(now_time[17:19]))[2:]
        if len(second) == 1:
            second = '0' + second
        now_time = (year + month + day + hour + minute + second).upper()  # 当前时间转换成16进制
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()  # VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[90:124], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换数据发送时间

        time.sleep(2)
        now_time_1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        year_1 = hex(int(now_time_1[2:4]))[2:]
        month_1 = hex(int(now_time_1[5:7]))[2:]
        if len(month_1) == 1:
            month_1 = '0' + month_1
        day_1 = hex(int(now_time_1[8:10]))[2:]
        if len(day_1) == 1:
            day_1 = '0' + day_1
        hour_1 = hex(int(now_time_1[11:13]))[2:]
        if len(hour_1) == 1:
            hour_1 = '0' + hour_1
        minute_1 = hex(int(now_time_1[14:16]))[2:]
        if len(minute_1) == 1:
            minute_1 = '0' + minute_1
        second_1 = hex(int(now_time_1[17:19]))[2:]
        if len(second_1) == 1:
            second_1 = '0' + second_1
        now_time_1 = (year_1 + month_1 + day_1 + hour_1 + minute_1 + second_1).upper()  # 当前时间转换成16进制
        binascii_data = binascii_data.replace(binascii_data[66:78], now_time_1)  # 替换信息采集时间
        binascii_data = binascii_data.replace(binascii_data[280:292], now_time_1)  # 替换信息采集时间
        binascii_data = binascii_data.replace(binascii_data[368:380], now_time_1)  # 替换信息采集时间
        # binascii_data = binascii_data.replace(binascii_data[90:124], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[342:350], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[350:358], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[358:366], mileage)  # 替换里程
        data = binascii_data[:-2]
        byte1 = int(str(data[0:2]), 16)
        for i in range(len(data) - 2):  # XOR异或运算得出BCC
            i = i + 2
            if i % 2 == 0:
                byte2 = int(str(data[i:i + 2]), 16)
                byte1 = x_o_r(byte1, byte2)[2:]
                byte1 = int(str(byte1), 16)
        BCC = (hex(byte1)[2:]).upper()
        if len(BCC) == 1:
            BCC = '0' + BCC
        binascii_data = data + BCC
        senddata = binascii.a2b_hex(binascii_data.strip())  # 将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_logout(self,vin):
        '''发送车辆退出：请求参数：车辆vin码、gateway地址、gateway端口'''
        binascii_data = '232304FE4A4C4630303030303030303030303030390100081308150E341E000191'
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        if len(month) == 1:
            month = '0' + month
        day = hex(int(now_time[8:10]))[2:]
        if len(day) == 1:
            day = '0' + day
        hour = hex(int(now_time[11:13]))[2:]
        if len(hour) == 1:
            hour = '0' + hour
        minute = hex(int(now_time[14:16]))[2:]
        if len(minute) == 1:
            minute = '0' + minute
        second = hex(int(now_time[17:19]))[2:]
        if len(second) == 1:
            second = '0' + second
        now_time = (year + month + day + hour + minute + second).upper()
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()
        binascii_data = binascii_data.replace(binascii_data[8:42] ,b2a_hex_vin)  #替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60],now_time)  #替换时间
        data = binascii_data[:-2]
        byte1 = int(str(data[0:2]), 16)
        for i in range(len(data) - 2):
            i = i + 2
            if i % 2 == 0:
                byte2 = int(str(data[i:i + 2]), 16)
                byte1 = x_o_r(byte1, byte2)[2:]
                byte1 = int(str(byte1), 16)
        BCC =  (hex(byte1)[2:]).upper()
        if len(BCC) == 1:
            BCC = '0' + BCC
        binascii_data =data + BCC
        senddata = binascii.a2b_hex(binascii_data.strip())
        return senddata

    def terminal_vehicle_report_incident(self, vin, Longitude, Latitude):
        '''发送车辆事件上报、车况自检和诊断数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # 报警事件报文
        binascii_data = '2323C1FE4C45544145454733584B4839323130303301003D14031E0B1F2601520514031E0B1F260006E5ACCB01B4D2B78014031E0B1F26001C9C41190000800000000000000000000000000000000000000000000018'

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]

        if len(month) == 1:
            month = '0' + month
        day = hex(int(now_time[8:10]))[2:]
        if len(day) == 1:
            day = '0' + day
        hour = hex(int(now_time[11:13]))[2:]
        if len(hour) == 1:
            hour = '0' + hour
        minute = hex(int(now_time[14:16]))[2:]
        if len(minute) == 1:
            minute = '0' + minute
        second = hex(int(now_time[17:19]))[2:]
        if len(second) == 1:
            second = '0' + second
        now_time = (year + month + day + hour + minute + second).upper()  # 当前时间转换成16进制
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()  # VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换采集时间
        binascii_data = binascii_data.replace(binascii_data[80:88], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[88:96], Latitude)  # 替换纬度
        data = binascii_data[:-2]
        byte1 = int(str(data[0:2]), 16)
        for i in range(len(data) - 2):  # XOR异或运算得出BCC
            i = i + 2
            if i % 2 == 0:
                byte2 = int(str(data[i:i + 2]), 16)
                byte1 = x_o_r(byte1, byte2)[2:]
                byte1 = int(str(byte1), 16)
        BCC = (hex(byte1)[2:]).upper()
        if len(BCC) == 1:
            BCC = '0' + BCC
        binascii_data = data + BCC
        print(binascii_data)
        senddata = binascii.a2b_hex(binascii_data.strip())  # 将16进制数字字符串转换为2进制数据
        return senddata

if __name__ == '__main__':
    Longitude = get_location.get_Longitude()
    Latitude = get_location.get_Latitude()
    BUFSIZ = 65535
    # host = ('111.231.213.96', 8111)  # 开发环境
    # host = ('10.50.187.52',30872) # 测试环境
    host = ('171.34.164.130',8111) # 测试环境
    lib = AinasciiA2bHex()
    # vin = ["LETAEEG3XKH921003"]
    vin = ["LETEDDE18FH000033"]
    # vin = ["LETEDDE16EH000093"]
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    # tcpCliSock.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
    tcpCliSock.connect(host)
    print ("开始发送车辆登录")
    tcpCliSock.send(lib.terminal_vehicle_login(vin[0]))
    time.sleep(2)
    print("开始发送车辆行程")

    num=0
    mileage = 2000
    for i in range(len(vin)):
        print ("发送第" + str(i)+ "辆k车登陆")

        for x in range(len(Latitude)):
            time.sleep(1)
            print("发送第" + str(i) + "辆实时数据：第" + str(x) + "次位置数据，经纬度数据为:" + (str(int(Longitude[x],16))) + "," + (str(int(Latitude[x],16))))
            tcpCliSock.send(lib.terminal_vehicle_upload_realtime(vin[i],Longitude[x],Latitude[x],mileage))

            num = num +1
            mileage = mileage + 1

            if num ==5:
                num = 0
                break
        # --------------------------------------------C1报警----------------------------------
        tcpCliSock.send(lib.terminal_vehicle_report_incident(vin[i],Longitude[x],Latitude[x]))
        # -------------------------------------------------------------------------------------
        print("发送车辆熄火")
        tcpCliSock.send(lib.terminal_vehicle_upload_realtime_flameout(vin[i],Longitude[x],Latitude[x],mileage))
        time.sleep(0.5)
        print("发送车辆退出登录")
        tcpCliSock.send(lib.terminal_vehicle_logout(vin[i]))
        time.sleep(0.5)
    # logging.info(tcpCliSock.recv(BUFSIZ).decode().strip())
        tcpCliSock.close()
        print ("发送完成")