# coding=utf-8
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
        # binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000138393836303243393939313630303032393134390118535657504541314137375631323137375630303030313231BF'
        binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000130393039383937363534343530303030303030300118535657504541314137375631323137375630303030313231BF'
        # binascii_data = '232301FE4A4C4630303030303030303030303030390100361308150E3314000138393836303331393336323030393238323935360118535657504541314137375631323137375630303030313231BF'
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
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100661308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100017804B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B0101410102400700000000000000000016'
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100661308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B0101410102400700000000000000000014'
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100761308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100004'
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E958271904001A20ED271A01034E2101024E2202012CB5'
        binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E9582719040000FE4A271A01034E2101024E2202012CB5'

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        speed = hex(random.randint(0, 999))[2:].upper()
        mileage = hex(mileage)[2:].upper()
        # alert = '0' + str(random.randint(1, 3)) + "".join(random.choice("789") for i in range(8))
        alert = '0' + '3' + "".join(random.choice("789") for i in range(8))
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
        # print now_time
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode() #VIN码转换成16进制
        # print b2a_hex_vin
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换时间
        binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        binascii_data = binascii_data.replace(binascii_data[234:244],alert)   #设置报警
        # binascii_data = binascii_data.replace('070000000000000000000','070200000010000000000')   #设置报警
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
        # print(f"实时的报文是:{binascii_data}")
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata



    def terminal_vehicle_upload_realtime_flameout(self,vin,Longitude,Latitude,mileage):
        '''发送车辆熄火数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100661308150E341E0102030101A9000007EE104507D055012E1E141200020101014154A4514A42103428990308070708000100013204B00100010100010101040200010001050006EEEB590261496E0601390FA1010F0F9B01014101024007000000000000000000B1'   #默认报文
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E9582719040000FE4A271A01034E2101024E2202012CB5'   #默认报文
        # 有错误的报文
        binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C01004CFF3C27160200D7271701012718040000E958271904FFFFFFFF271A01034E2101024E2202012CB5'   #默认报文

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
        # print now_time
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode() #VIN码转换成16进制
        # print b2a_hex_vin
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换时间
        binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        # binascii_data = binascii_data.replace('07000000000000000000', '07010011100000000000')  # 设置报警
        binascii_data = binascii_data.replace('070000000000', '070300001000')  # 设置报警
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

    def terminal_vehicle_upload_realtime_location(self,vin,Longitude,Latitude):
        '''发送车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''

        binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C0100FEFF3C27160200D7271701012718040000E958271904FFFFFFFF271A01034E2101024E2202012CB5'   #默认报文
        # binascii_data ='232302FE4A4C4630303030303030303030303030390100761308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100004'

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        speed = hex(random.randint(0,999))[2:].upper()
        if len(speed)==3:
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
        # print now_time
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode() #VIN码转换成16进制
        # print b2a_hex_vin
        binascii_data = binascii_data.replace(binascii_data[8:42] ,b2a_hex_vin)  #替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60],now_time)  #替换时间
        binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
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
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_report_incident(self, vin,Longitude,Latitude,mileage,mileage_end):
        '''发送车辆事件上报、车况自检和诊断数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # 新能源报警事件
        # binascii_data = '2323C1FE4C4554454444453130454830303030303201002F14031E0B1F26050006E5ACCB01B4D2B780001C9C41198000000000000000000000000000000000000000000000000030'

        #  车况自检报文
        # binascii_data = '2323C0FE49535554455354323538343039333136370100161401110D3104050100000D00000300000900000E000040'

        # 驾驶行为报文
        binascii_data = '2323C2FE4A4C46303030303030303030303030303901003D1401130B0B1E1401190B1A32000007D00633F38E01D406781401190B1F3207D60633EB9201D39456007800050008000700060005000400030002000A0291'

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
        # print(now_time)
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()  # VIN码转换成16进制
        # print(b2a_hex_vin)
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换采集时间
        # binascii_data = binascii_data.replace(binascii_data[64:72], Longitude)  # 替换经度
        # binascii_data = binascii_data.replace(binascii_data[72:80], Latitude)  # 替换纬度
        # -----------------------------------------------------------------------------------------------
        # 驾驶行为专用
        time.sleep(2)
        now_time_1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        year_1 = hex(int(now_time_1[2:4]))[2:]
        month = hex(int(now_time_1[5:7]))[2:]
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
        day = hex(int(now_time_1[8:10]))[2:]
        if len(day) == 1:
            day = '0' + day
        hour = hex(int(now_time_1[11:13]))[2:]
        if len(hour) == 1:
            hour = '0' + hour
        minute = hex(int(now_time_1[14:16]))[2:]
        if len(minute) == 1:
            minute = '0' + minute
        second = hex(int(now_time_1[17:19]))[2:]
        if len(second) == 1:
            second = '0' + second
        now_time_1 = (year_1 + month + day + hour + minute + second).upper()  # 当前时间转换成16进制
        binascii_data = binascii_data.replace(binascii_data[60:72], now_time_1)  # 替换行程时间
        binascii_data = binascii_data.replace(binascii_data[72:80], mileage)  # 替换
        binascii_data = binascii_data.replace(binascii_data[80:88], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[88:96], Latitude)  # 替换纬度
        # ----
        time.sleep(2)
        now_time_2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        year_2 = hex(int(now_time_2[2:4]))[2:]
        month = hex(int(now_time_2[5:7]))[2:]
        mileage_end = hex(mileage_end)[2:].upper()
        if len(mileage_end) != 8:
            m = (8 - len(mileage_end)) * str(0)
        mileage_end = m + mileage_end
        if len(speed) == 3:
            speed = "0" + speed
        if len(speed) == 2:
            speed = "00" + speed
        if len(speed) == 1:
            speed = "000" + speed
        if len(month) == 1:
            month = '0' + month
        day = hex(int(now_time_2[8:10]))[2:]
        if len(day) == 1:
            day = '0' + day
        hour = hex(int(now_time_2[11:13]))[2:]
        if len(hour) == 1:
            hour = '0' + hour
        minute = hex(int(now_time_2[14:16]))[2:]
        if len(minute) == 1:
            minute = '0' + minute
        second = hex(int(now_time_2[17:19]))[2:]
        if len(second) == 1:
            second = '0' + second
        now_time_2 = (year_2 + month + day + hour + minute + second).upper()  # 当前时间转换成16进制
        binascii_data = binascii_data.replace(binascii_data[96:108], now_time_2)  # 替换行程结束时间
        binascii_data = binascii_data.replace(binascii_data[108:116], mileage_end)  # 替换结束里程
        binascii_data = binascii_data.replace(binascii_data[116:124], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[124:132], Latitude)  # 替换纬度
        # ---------------------------------------------------------------------------------------------------------------

        # -----------------------------------------------------------------------------------------------
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
    # host = ('111.231.210.113', 8111)  # 开发环境
    # host = ('10.50.187.52',30873) # 测试环境
    host = ('171.34.164.130',8112) # 测试环境
    lib = AinasciiA2bHex()
    # vin = ['ISUTEST2564371809','ISUTEST2985067431','ISUTEST3806591742','ISUTEST2731680954','ISUTEST6381245790'
    #     ,'ISUTEST3490627158','ISUTEST6215038947','ISUTEST6758230941','ISUTEST4960752138',
    # 'ISUTEST4690321587','ISUTEST4068751293','ISUTEST8065972134','ISUTEST7415908632','ISUTEST2379084615',
    # 'ISUTEST8052134769','ISUTEST8629475103','ISUTEST2847596031','ISUTEST1570483926','ISUTEST6498530721','ISUTEST3521079648']
    # vin = ["LETADDE16EH000237"]
    # vin = ["ISUTEST2584093167"]
    vin = ["ISUTEST6015798324"]
    # vin = ["LA9CEAG29KHLET930"]
    # vin = ["LETEDDE19FH000039"]
    # vin = ["LETADDE17EH000408"]
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    # tcpCliSock.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
    tcpCliSock.connect(host)
    print ("开始发送车辆登录")
    tcpCliSock.send(lib.terminal_vehicle_login(vin[0]))
    time.sleep(2)
    print("开始发送车辆行程")

    num=0
    mileage = 20000
    mileage_end = 40000
    for i in range(len(vin)):
        print ("发送第" + str(i)+ "辆k车登陆")
        # tcpCliSock.send(lib.terminal_vehicle_login(vin[i]))
        for x in range(len(Latitude)):
            time.sleep(1)
            print("发送第" + str(i) + "辆实时数据：第" + str(x) + "次位置数据，经纬度数据为:" + (str(int(Longitude[x],16))) + "," + (str(int(Latitude[x],16))))
            tcpCliSock.send(lib.terminal_vehicle_upload_realtime(vin[i],Longitude[x],Latitude[x],mileage))
            num = num +1
            mileage = mileage + 1
            if num ==1:
                num = 0
                break
        #
        #------------------------------------------------------------------------------------
        # --------------------------------报警C1-----------------------------------------------
        # tcpCliSock.send(lib.terminal_vehicle_report_incident(vin[i],Longitude[x],Latitude[x]))
        # time.sleep(3)
        # tcpCliSock.send(lib.terminal_vehicle_report_incident(vin[0])
        # tcpCliSock.send(lib.terminal_vehicle_report_incident(vin[0],Longitude[x],Latitude[x],mileage,mileage_end))

        print("发送车辆熄火")
        # tcpCliSock.send(lib.terminal_vehicle_upload_realtime_flameout(vin[i],Longitude[x],Latitude[x],mileage))
        tcpCliSock.send(lib.terminal_vehicle_upload_realtime_flameout(vin[i],Longitude[x],Latitude[x],mileage))
        time.sleep(0.5)
        print("发送车辆退出登录")
        tcpCliSock.send(lib.terminal_vehicle_logout(vin[i]))
        time.sleep(0.5)
    # logging.info(tcpCliSock.recv(BUFSIZ).decode().strip())
        tcpCliSock.close()
        print ("发送完成")


