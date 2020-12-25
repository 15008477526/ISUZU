import time
import binascii
import logging
from socket import *
from isuzu import get_location
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
        # 系能源LA9CEAG29KHLET930报文
        # binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000138393836303243393939313630303032393134390118535657503839383630333139333632303039323832393536BF'
        # 新能源798324登录报文
        binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000130393039383937363534343530303030303030300118535657504541314137375631323137375630303030313231BF'
        # binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000138393836313131383239303033313936363733370118535657504541314137375631323137375630303030313231BF'
        # UAT环境LISUZUPN100TEST12
        # binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000138393836313131383239303033313936363733370118535657504541314137375631323137375630303030313231BF'
        # 新能源798325报文
        # binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000130393039383937363534343531313131303030300118535657504541314137375631323137375630303030313231BF'
        # 燃油车LETAEEG3XKH921003
        # binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000138393836303331393336323030393238323935360118535657503839383630333139343732303836363633343036BF'
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
        # print now_time
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()
        # print b2a_hex_vin
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
        print(f"登录的报文是:{binascii_data}")
        senddata = binascii.a2b_hex(binascii_data.strip())
        return senddata

    def terminal_vehicle_upload_realtime(self,vin,Longitude,Latitude,mileage):
        '''发送车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # 新能源实时报文
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E95827190400001969271A01034E2101024E2202012CB5'
        binascii_data = '232302FE4A4C4630303030303030303030303030390100821308150E331E0101030101A9000007D0104507D060012E1E141200020201014154A4514A4210342899020142500041A450102430000307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B0101410102400700000000000110001000011000000101000110000110001000B5'
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100821308150E331E0101030101A9000007D0104507D060012E1E141200020201014154A4514A4210342899020142500041A450102430000307080708000100011E04B00100010100010101040100010001050100000000000000000601390FA1010F0F9B0101410102400700000000000110001000011000000101000110000110001000B5' #经纬度0的报文

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        speed = hex(random.randint(0, 999))[2:].upper()
        mileage = hex(mileage)[2:].upper()
        # alert = '0' + str(random.randint(1, 3)) + "".join(random.choice("789") for i in range(8))
        # alert = '0' + '2' + "".join(random.choice("789") for i in range(8))
        # alert = '038808880F'
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
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode() #VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换时间

        binascii_data = binascii_data.replace(binascii_data[210:218], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[218:226], Latitude)  # 替换纬度

        # binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        # binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度

        binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        binascii_data = binascii_data.replace('070000000000', '070300000080')  # 设置报警 SOC低报警
        # binascii_data = binascii_data.replace(binascii_data[234:244],alert)   #设置报警
        # binascii_data = binascii_data.replace('070000000000', '070300030091')  # 设置报警
        binascii_data = binascii_data.replace(binascii_data[72:80], mileage)  #替换里程
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
        print(f"实时的报文是:{binascii_data}")
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata


    def terminal_vehicle_upload_realtime_1(self,vin,Longitude,Latitude):
        '''发送车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # 新能源实时报文
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E95827190400001969271A01034E2101024E2202012CB5'
        binascii_data = '232302FE4A4C4630303030303030303030303030390100821308150E331E0101030101A9000007D0104507D060012E1E141200020201014154A4514A4210342899020142500041A450102430000307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B0101410102400700000000000110001000011000000101000110000110001000B5'
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100821308150E331E0101030101A9000007D0104507D060012E1E141200020201014154A4514A4210342899020142500041A450102430000307080708000100011E04B00100010100010101040100010001050100000000000000000601390FA1010F0F9B0101410102400700000000000110001000011000000101000110000110001000B5' #经纬度0的报文

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        speed = hex(random.randint(0, 999))[2:].upper()
        # mileage = hex(mileage)[2:].upper()

        # if len(mileage) != 8:
        #     m = (8 - len(mileage)) * str(0)
        # mileage = m + mileage
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
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode() #VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换时间
        # binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[210:218], Longitude)  # 替换经度
        # binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[218:226], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        binascii_data = binascii_data.replace('070000000000', '070300000080')  # 设置报警 SOC低报警
        # binascii_data = binascii_data.replace(binascii_data[234:244],alert)   #设置报警
        # binascii_data = binascii_data.replace('070000000000', '070300030091')  # 设置报警
        # binascii_data = binascii_data.replace(binascii_data[72:80], mileage)  #替换里程
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
        print(f"实时的报文是:{binascii_data}")
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_realtime_info(self,vin):
        '''发送新能源车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''

        # binascii_data = '2323C5FE4C4554454444453138464830303030333301006A00681409090F112C271102050527120155271302000027140F450ABA0AB95432005D005C005B005A2715068070605040302716020043271701022718040000001E271904FFFFFFFF271A0102271B0102271C020032271D0128271E0102271F01202720010227210201501A' # 车门
        # binascii_data = '2323C5FE4C4554454444453138464830303030333301006A00681409090F112C271102050527120155271302000027140F450ABA0AB95432005D005C005B005A2715068070605040302716020043271701022718040000001E271904FFFFFFFF271A0103271B0102271C020032271D0128271E0102271F01202720010227210201501A' # 车门
        binascii_data = '2323C5FE4C4554454444453138464830303030333301006A00681409090F112C271102050527120155271302000027140F000000000000000028001E0014000A2715068070605040302716020043271701022718040000001E271904FFFFFFFF271A0103271B0102271C020032271D0128271E0102271F01202720010227210201501A' # 车门

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        speed = hex(random.randint(0, 999))[2:].upper()
        # mileage = hex(mileage)[2:].upper()
        #
        # if len(mileage) != 8:
        #     m = (8 - len(mileage)) * str(0)
        # mileage = m + mileage
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
        binascii_data = binascii_data.replace(binascii_data[52:64], now_time)  # 替换数据发送时间

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
        print(f'车况报文是:{binascii_data}')
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_realtime_info_end(self, vin):
        '''发送新能源车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        binascii_data = '2323C5FE4C4554454444453138464830303030333301006A00681409090F112C271102050527120155271302000027140F450ABA0AB95432005D005C005B005A2715068070605040302716020043271701022718040000001E271904FFFFFFFF271A0102271B0102271C020032271D0128271E0102271F01202720010227210201501A'
        # binascii_data = '2323C5FE4C4554454444453138464830303030333301006A00681409090F112C271102050527120155271302000027140F00FFFFFFFF0000FFFFFFFFFFFFFFFF2715068070605040302716020043271701022718040000001E271904FFFFFFFF271A0103271B0102271C020032271D0128271E0102271F01202720010227210201501A'

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        speed = hex(random.randint(0, 999))[2:].upper()
        # mileage = hex(mileage)[2:].upper()
        #
        # if len(mileage) != 8:
        #     m = (8 - len(mileage)) * str(0)
        # mileage = m + mileage
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
        # print(now_time)
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()  # VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[52:64], now_time)  # 替换数据发送时间

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
        print(f'车况报文是:{binascii_data}')
        senddata = binascii.a2b_hex(binascii_data.strip())  # 将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_upload_realtime_flameout(self,vin,Longitude,Latitude,mileage):
        '''发送车辆熄火数据：请求参数：车辆vin码、gateway地址、gateway端口'''

        # binascii_data = '232302FE4A4C4630303030303030303030303030390100821308150E331E0102030101A9000007D0104507D060012E1E141200020201014154A4514A4210342899020142500041A450102430000307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B0101410102400700000000000110001000011000000101000110000110001000B5'   #默认报文
        binascii_data = '232302FE4A4C4630303030303030303030303030390100841308150E331E0102030101A9000007D0104507D050012E1E141200020201014154A4514A4210342899020142500041A450102430000307080708000100031E1A0904B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B0101410102400700000000000110001000011000000101000110000110001000B5'   #默认报文
        # 有错误的报文无效车速、里程
        # binascii_data = '232302FE49535554455354363031353739383332340100C614040F10372401020301FFFFFFFFFFFF104507D0FF012E1E141200020101014154A4514A4210342899030708070800010001804152020001012200010104010001000105000635017701D3EE240601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102000527120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D727170102271804FFFFFFFF271904FFFFFFFF271A01FF4E2101024E2202012C08'   #默认报文
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        # speed = hex(random.randint(0, 999))[2:].upper()
        mileage = hex(mileage)[2:].upper()
        if len(mileage) != 8:
            m = (8 - len(mileage)) * str(0)
        mileage = m + mileage

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
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode() #VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换时间
        # binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        # binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        # binascii_data = binascii_data.replace(binascii_data[210:218], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[214:222], Longitude)  # 替换经度
        # binascii_data = binascii_data.replace(binascii_data[218:226], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[222:230], Latitude)  # 替换纬度
        # binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        # binascii_data = binascii_data.replace('07000000000000000000', '07010011100000000000')  # 设置报警
        # binascii_data = binascii_data.replace('070000000000', '07030007FFFF')  # 设置报警
        binascii_data = binascii_data.replace('070000000000', '070000000000')
        binascii_data = binascii_data.replace(binascii_data[72:80], mileage)  # 替换里程
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
        print(f"熄火的报文是:{binascii_data}")
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_logout(self,vin):
        '''发送车辆退出：请求参数：车辆vin码、gateway地址、gateway端口'''
        # binascii_data = '232304FE4A4C4630303030303030303030303030390100081308150E341E001A8A'
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
        # print now_time
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()
        # print b2a_hex_vin
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
        print(f"退出的报文是:{binascii_data}")
        senddata = binascii.a2b_hex(binascii_data.strip())
        return senddata

if __name__ == '__main__':
    Longitude = get_location.get_Longitude()
    Latitude = get_location.get_Latitude()
    BUFSIZ = 65535

    host = ('192.168.201.135',32353)  # UAT_环境
    lib = AinasciiA2bHex()
    vin = ["ISUTEST6015798324"]
    # vin = ["ISUTEST6015798325"]
    # vin = ["LISUZUPN100TEST12"]
    # vin = ["ISUTEST0154376298"]
    # vin = ["LA9CEAG29KHLET930"]
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    # tcpCliSock.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
    tcpCliSock.connect(host)
    print("开始发送车辆登录")
    tcpCliSock.send(lib.terminal_vehicle_login(vin[0]))
    time.sleep(2)
    print("开始发送车辆行程")
    num = 0
    mileage = 2000
    for i in range(len(vin)):
        print("发送第" + str(i) + "辆k车登陆")

        for x in range(len(Latitude)):
            time.sleep(1)
            print("发送第" + str(i) + "辆实时数据：第" + str(x) + "次位置数据，经纬度数据为:" + (str(int(Longitude[x], 16))) + "," + (str(int(Latitude[x], 16))))
            tcpCliSock.send(lib.terminal_vehicle_realtime_info(vin[i]))
            tcpCliSock.send(lib.terminal_vehicle_upload_realtime(vin[i], Longitude[x], Latitude[x], mileage))


            num = num + 1
            mileage = mileage + 100
            if num == 2:
                num = 0
                break
        # time.sleep(3)
        # tcpCliSock.send(lib.terminal_vehicle_realtime_info(vin[i]))
        # tcpCliSock.send(lib.terminal_vehicle_upload_realtime_1(vin[i], Longitude[x], Latitude[x]))
        time.sleep(3)
        print("发送车辆熄火")
        time.sleep(1)

        tcpCliSock.send(lib.terminal_vehicle_realtime_info_end(vin[i]))
        tcpCliSock.send(lib.terminal_vehicle_upload_realtime_flameout(vin[i], Longitude[x], Latitude[x],mileage))

        time.sleep(1)
        print("发送车辆退出登录")
        tcpCliSock.send(lib.terminal_vehicle_logout(vin[i]))
        time.sleep(0.5)

        tcpCliSock.close()
        print("发送完成")