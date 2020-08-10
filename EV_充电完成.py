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
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100661308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B0101410102400700000000000000000014'
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100761308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100004'
        # 新能源+实时车况80的实时报文
        binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D061012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E95827190400001969271A01034E2101024E2202012CB5'

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
        binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        # binascii_data = binascii_data.replace(binascii_data[234:244],alert)   #设置报警
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
        print(f"实时的报文是:{binascii_data}")
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_upload_realtime_1(self,vin,Longitude,Latitude,mileage):
        '''发送车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100661308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B0101410102400700000000000000000014'
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100761308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100004'
        # 新能源+实时车况80的实时报文
        binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D061012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E95827190400001969271A01034E2101024E2202012CB5'

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
        binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        # binascii_data = binascii_data.replace(binascii_data[234:244],alert)   #设置报警
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
        print(f"实时的报文是:{binascii_data}")
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_upload_realtime_flameout(self,vin,Longitude,Latitude,mileage):
        '''发送车辆熄火数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100661308150E341E0102030101A9000007EE104507D055012E1E141200020101014154A4514A42103428990308070708000100013204B00100010100010101040200010001050006EEEB590261496E0601390FA1010F0F9B01014101024007000000000000000000B1'   #默认报文
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E9582719040000FE4A271A01034E2101024E2202012CB5'   #默认报文
        # 有错误的报文
        binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0101030101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C01004CFF3C27160200D7271701022718040000E958271904FFFFFFFF271A01034E2101024E2202012CB5'   #默认报文

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
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode() #VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换时间
        binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        # binascii_data = binascii_data.replace('07000000000000000000', '07010011100000000000')  # 设置报警
        # binascii_data = binascii_data.replace('070000000000', '070300001000')  # 设置报警
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

    def terminal_vehicle_upload_realtime_chargecomplete(self,vin,Longitude,Latitude):
        '''发送车辆充电完成数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # binascii_data = '232302FE4A4C46303030303030303030303030303901015F1308150E331E0102040101A9000007D01045000050012E1E141200020101014154A4514A42103428990300010001000100010100010100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B01014101024007000000000000000000080101104528AA00680001680FA00F9F0FA00F9F0FA00F9F0F9F0F9E0F9F0F9F0F9F0F9F0F9E0F9F0F9B0F9F0F9F0F9F0F9F0F9E0F9F0F9F0F9F0F9F0F9F0F9F0F9F0FA00F9F0FA00F9F0FA00F9F0FA00F9F0FA00F9F0FA00F9F0F9F0F9F0F9F0F9F0F9F0F9F0F9F0F9F0F9E0F9F0F9E0F9F0F9E0FA00F9F0FA00F9F0FA10F9F0FA00F9F0F9F0F9F0FA00FA00F9E0FA00F9F0FA00FA00FA00F9F0FA00F9F0F9F0F9F0F9F0F9F0F9F0F9F0F9E0F9E0F9F0F9E0F9E0F9D0F9E0F9F0F9E0F9F0F9E0F9E0F9E0F9E0F9F0F9E0F9D0F9D0F9E0F9D0F9E0F9E0F9E0F9F0F9E090101001041404140414041404141414141414141800005010101010116'   #默认报文
        # binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0102040101A9000007D0104507D060012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E9582719040000FE4A271A01034E2101024E2202012CB5'   #默认报文
        # 错误SOC，里程
        binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E01020401FFFFFFFFFFFF104507D0FF012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E9582719040000FE4A271A01034E2101024E2202012CB5'   #默认报文
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  #获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        # soc = "0834" + hex(soc)[2:].upper()
        # if len(soc) == 1:
        #     soc = '0' + soc
        if len(month) == 1:
            month = '0' + month
        day = hex(int(now_time[8:10]))[2:]
        if len(day) == 1:
            day = '0' + day
        hour = hex(int(now_time[11:13]))[2:]
        if len(hour) == 1:
            hour = '0' + hour
        minute = hex(int(now_time[14:16])+5)[2:]
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
        # binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        # binascii_data = binascii_data.replace(binascii_data[84:90], soc)  # 替换SOC
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
        print(binascii_data)
        senddata = binascii.a2b_hex(binascii_data.strip())  #将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_upload_realtime_recharge(self, vin, Longitude, Latitude, soc):
        '''发送车辆停车充电数据：请求参数：车辆vin码、gateway地址、gateway端口'''
        # binascii_data = '232302FE4A4C46303030303030303030303030303901015F1308150E331E0102010101A9000007D01045083430012E1E141200020101014154A4514A42103428990300010001000100010100010100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B01014101024007000000000000000000080101104528AA00680001680FA00F9F0FA00F9F0FA00F9F0F9F0F9E0F9F0F9F0F9F0F9F0F9E0F9F0F9B0F9F0F9F0F9F0F9F0F9E0F9F0F9F0F9F0F9F0F9F0F9F0F9F0FA00F9F0FA00F9F0FA00F9F0FA00F9F0FA00F9F0FA00F9F0F9F0F9F0F9F0F9F0F9F0F9F0F9F0F9F0F9E0F9F0F9E0F9F0F9E0FA00F9F0FA00F9F0FA10F9F0FA00F9F0F9F0F9F0FA00FA00F9E0FA00F9F0FA00FA00FA00F9F0FA00F9F0F9F0F9F0F9F0F9F0F9F0F9F0F9E0F9E0F9F0F9E0F9E0F9D0F9E0F9F0F9E0F9F0F9E0F9E0F9E0F9E0F9F0F9E0F9D0F9D0F9E0F9D0F9E0F9E0F9E0F9F0F9E090101001041404140414041404141414141414141800005010101010116'   #默认报文
        binascii_data = '232302FE4A4C4630303030303030303030303030390100C61308150E331E0102010101A9000007D0104507D02A012E1E141200020101014154A4514A42103428990307080708000100011E04B00100010100010101040100010001050006EEED8E02614C3F0601390FA1010F0F9B010141010240070000000000011000100001100000010100011000011000100080004D271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701012718040000E9582719040000FE4A271A01034E2101024E2202012CB5'  # 默认报文
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        year = hex(int(now_time[2:4]))[2:]
        month = hex(int(now_time[5:7]))[2:]
        soc = "0834" + hex(soc)[2:].upper()
        if len(soc) == 1:
            soc = '0' + soc
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
        time.sleep(1)
        now_time = (year + month + day + hour + minute + second).upper()  # 当前时间转换成16进制
        b2a_hex_vin = binascii.b2a_hex(vin.encode()).decode()  # VIN码转换成16进制
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换时间
        binascii_data = binascii_data.replace(binascii_data[186:194], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[194:202], Latitude)  # 替换纬度
        # binascii_data = binascii_data.replace(binascii_data[68:72], speed)  # 替换车速
        binascii_data = binascii_data.replace(binascii_data[84:90], soc)  # 替换SOC
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
    # host = ('111.231.210.113', 8111)  # 开发环境
    # host = ('10.50.187.52',30873) # 测试环境
    host = ('171.34.164.130', 8112)  # 测试环境
    lib = AinasciiA2bHex()
    vin = ["ISUTEST6015798324"]
    # vin = ["LA9CEAG29KHLET930"]
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    # tcpCliSock.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
    tcpCliSock.connect(host)
    print("开始发送车辆登录")
    tcpCliSock.send(lib.terminal_vehicle_login(vin[0]))
    time.sleep(2)
    print("开始发送车辆行程")
    num = 0
    mileage = 45000
    soc=90
    for i in range(len(vin)):
        print("发送第" + str(i) + "辆k车登陆")
        # tcpCliSock.send(lib.terminal_vehicle_login(vin[i]))
        for x in range(len(Latitude)):
            time.sleep(1)
            print("发送第" + str(i) + "辆实时数据：第" + str(x) + "次位置数据，经纬度数据为:" + (str(int(Longitude[x], 16))) + "," + (str(int(Latitude[x], 16))))
            # tcpCliSock.send(lib.terminal_vehicle_upload_realtime(vin[i], Longitude[x], Latitude[x], mileage))
            # tcpCliSock.send(lib.terminal_vehicle_upload_realtime(vin[i], Longitude[x], Latitude[x],mileage))
            tcpCliSock.send(lib.terminal_vehicle_upload_realtime_recharge(vin[i],Longitude[x],Latitude[x],soc))
            # tcpCliSock.send(lib.terminal_vehicle_upload_realtime_chargecomplete(vin[i], Longitude[x], Latitude[x]))
            num = num + 1
            mileage = mileage + 1
            if num == 1:
                num = 0
                break
        time.sleep(2)
        # tcpCliSock.send(lib.terminal_vehicle_upload_realtime_1(vin[i], Longitude[x], Latitude[x], mileage))
        time.sleep(1)
        # tcpCliSock.send(lib.terminal_vehicle_upload_realtime_chargecomplete(vin[i],Longitude[x],Latitude[x],soc))
        tcpCliSock.send(lib.terminal_vehicle_upload_realtime_chargecomplete(vin[i],Longitude[x],Latitude[x]))

        print("发送车辆熄火")
        # tcpCliSock.send(lib.terminal_vehicle_upload_realtime_flameout(vin[i], Longitude[x], Latitude[x], mileage))
        time.sleep(0.5)
        print("发送车辆退出登录")
        tcpCliSock.send(lib.terminal_vehicle_logout(vin[i]))
        time.sleep(0.5)
        # logging.info(tcpCliSock.recv(BUFSIZ).decode().strip())
        tcpCliSock.close()
        print("发送完成")