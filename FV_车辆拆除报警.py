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
        # binascii_data = '232301FE4C4554454444453130454830303030303201001C1401150F282000013839383630333139343732303836363633343036B2'
        # UAT环境ISUTEST5468729310
        # binascii_data = '232301FE4C4554454444453130454830303030303201001C1401150F282000013239323938393736353434353131313130303030B2'
        # 燃油车FH000033
        binascii_data = '232301FE4C4554454444453130454830303030303201001C1401150F282000013839383630393139373130303235303537383234B2'
        # 燃油车EH000093
        # binascii_data = '232301FE4C4554454444453130454830303030303201001C1401150F282000013839383631393139373130303235303537383234B2'

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
        # 三元催化
        # binascii_data = '232302FE4C455445444445313045483030303030320100B21401150F28210001011401150F28210000002500C34C45544544444531304548303030303032544553545F56455253494F4E5F56312E303043564E5F56414C5545303030303030303030495550525F56414C554530303030303030303030303030303030303030303030303030300111111111031401150F2821330098968B056100BB287D2913291200433443000633F38E01D40678000007D0801401150F282109600000005020000000150000003200A9AC'
        # 实时02数据
        binascii_data = '232302FE4C455445444445313846483030303033330100BB1405120E36200001011405120E36200000002500C34C45544544444531384648303030303333544553545F56455253494F4E5F56312E303043564E5F56414C5545303030303030303030495550525F56414C55453030303030303030303030303030303030303030303030303030020647F009C10F2901021405120E3620330098968B056100BB287D29138000E600A900A800204334000635017701D3EE2400000802801405120E362009600000005020000000150000003200A9CE'  # 带有故障码
        # binascii_data = '232302FE4C45545945454732334C483031343330390300B3140616111E2D1FE2011406140F1A340100DEA01EA04C45545945454732334C483031343330394D4431434338373820344A204830303230300678B49530303030303030303030303030300000001C00000000000000000000000000000000000000000000000000000000001700000002140616111E2D0000C77D8200000000FFFFFFFF4A00A0259925C6000043000006E5A5DA01B4DA560000001E80140616111E2D0900000000284800000000000000002720B6' # 不带有故障码

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
        # -----------------------------------------------------------------------------------------------------
        binascii_data = binascii_data.replace(binascii_data[288:300], now_time_1)  # 替换信息采集时间
        binascii_data = binascii_data.replace(binascii_data[376:388], now_time_1)  # 替换信息采集时间
        binascii_data = binascii_data.replace(binascii_data[350:358], Longitude)  # 替换经度  实时02开启
        binascii_data = binascii_data.replace(binascii_data[358:366], Latitude)  # 替换纬度   实时02开启
        binascii_data = binascii_data.replace(binascii_data[366:374], mileage)  # -------  有两个故障
        # -----------------------------------------------------------------------------------------------------------
        # binascii_data = binascii_data.replace(binascii_data[272:284], now_time_1)  # 替换信息采集时间
        # binascii_data = binascii_data.replace(binascii_data[360:372], now_time_1)  # 替换信息采集时间   实时02 开启
        # binascii_data = binascii_data.replace(binascii_data[334:342], Longitude)  # 替换经度  实时02开启
        # binascii_data = binascii_data.replace(binascii_data[342:350], Latitude)  # 替换纬度   实时02开启
        # binascii_data = binascii_data.replace(binascii_data[350:358], mileage)  # 替换里程    --无故障
        # *******************************************************************************************************************
        # binascii_data = binascii_data.replace(binascii_data[280:292], now_time_1)  # 替换信息采集时间
        # binascii_data = binascii_data.replace(binascii_data[358:370], now_time_1)  # 替换信息采集时间     三元催化开启
        # binascii_data = binascii_data.replace(binascii_data[332:340], Longitude)  # 替换经度  三元催化开启
        # binascii_data = binascii_data.replace(binascii_data[340:348], Latitude)  # 替换纬度   三元催化
        # binascii_data = binascii_data.replace(binascii_data[348:356], mileage)  # 替换里程    三元催化
        #**************************************************************************************************************************
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
        # OBD错误VIN码报文
        # binascii_data = '232302FE4C455445444445313045483030303030320100F41401150F28210001011401150F28210000002500C33F3F3F3F3F3F3F3F3F3F3F3F3F3F3F3F3F544553545F56455253494F4E5F56312E303043564E5F56414C5545303030303030303030495550525F56414C554530303030303030303030303030303030303030303030303030300111111111021401150F2821330098968B056100BB287D29134700E64334435D007878BE000633F38E01D40678000007D0801401150F2821004C271102100127120111271302001527140F0014001400140014000000140014002715063C3C3C3C3C3C27160200D7271701022718040000E958271904000000AB271A01033E8101603E820120CB'
        # 三元催化
        # binascii_data = '232302FE4C455445444445313045483030303030320100B21401150F28210001011401150F28210000002500C34C45544544444531304548303030303032544553545F56455253494F4E5F56312E303043564E5F56414C5545303030303030303030495550525F56414C554530303030303030303030303030303030303030303030303030300111111111031401150F2821330098968B056100BB287D2913291200433443000633F38E01D40678000007D0801401150F282109600000005020000000150000003200A9AC'
        # 实时02数据
        binascii_data = '232302FE4C455445444445313846483030303033330100BB1405120E36200001011405120E36200000002500C34C45544544444531384648303030303333544553545F56455253494F4E5F56312E303043564E5F56414C5545303030303030303030495550525F56414C55453030303030303030303030303030303030303030303030303030020647F009203FF428021405120E3620330098968B056100BB287D29138000E600A900A800204334000635017701D3EE2400000802801405120E362009600000005020000000150000003200A9CE'  # 带有故障码
        # binascii_data = '232302FE4C45545945454732334C483031343330390300B3140616111E2D1FE2011406140F1A340100DEA01EA04C45545945454732334C483031343330394D4431434338373820344A204830303230300678B49530303030303030303030303030300000001C00000000000000000000000000000000000000000000000000000000001700000002140616111E2D0000C77D8200000000FFFFFFFF4A00A0259925C6000043000006E5A5DA01B4DA560000001E80140616111E2D0900000000284800000000000000002720B6' # 不带有故障码

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
        # print(now_time)
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
        # -----------------------------------------------------------------------------------------------------
        binascii_data = binascii_data.replace(binascii_data[288:300], now_time_1)  # 替换信息采集时间
        binascii_data = binascii_data.replace(binascii_data[376:388], now_time_1)  # 替换信息采集时间
        binascii_data = binascii_data.replace(binascii_data[350:358], Longitude)  # 替换经度  实时02开启
        binascii_data = binascii_data.replace(binascii_data[358:366], Latitude)  # 替换纬度   实时02开启
        binascii_data = binascii_data.replace(binascii_data[366:374], mileage)  # -------  有两个故障
        # -----------------------------------------------------------------------------------------------------------
        # binascii_data = binascii_data.replace(binascii_data[272:284], now_time_1)  # 替换信息采集时间
        # binascii_data = binascii_data.replace(binascii_data[360:372], now_time_1)  # 替换信息采集时间   实时02 开启
        # binascii_data = binascii_data.replace(binascii_data[334:342], Longitude)  # 替换经度  实时02开启
        # binascii_data = binascii_data.replace(binascii_data[342:350], Latitude)  # 替换纬度   实时02开启
        # binascii_data = binascii_data.replace(binascii_data[350:358], mileage)  # 替换里程    --无故障
        # *******************************************************************************************************************
        # binascii_data = binascii_data.replace(binascii_data[280:292], now_time_1)  # 替换信息采集时间
        # binascii_data = binascii_data.replace(binascii_data[358:370], now_time_1)  # 替换信息采集时间     三元催化开启
        # binascii_data = binascii_data.replace(binascii_data[332:340], Longitude)  # 替换经度  三元催化开启
        # binascii_data = binascii_data.replace(binascii_data[340:348], Latitude)  # 替换纬度   三元催化
        # binascii_data = binascii_data.replace(binascii_data[348:356], mileage)  # 替换里程    三元催化
        # **************************************************************************************************************************
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
        print(f'实时报文是:{binascii_data}')
        senddata = binascii.a2b_hex(binascii_data.strip())  # 将16进制数字字符串转换为2进制数据
        return senddata

    def terminal_vehicle_realtime_info(self,vin):
        '''发送燃油车车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''

        # binascii_data = '2323C5FE4C45545945454732334C4830313433303901006A0068140616111E2D271102000127120155271302000027140F0000000000000000000000000000002715060000000000002716020043271701012718040000001E271904FFFFFFFF271A0102271B0102271C020032271D0128271E0102271F010027200102272102015029'
        binascii_data = '2323C5FE4C45545945454732334C4830313433303901006A0068140616111E2D271102000127120155271302000027140F0000000000000000000000000000002715060000000000002716020043271701012718040000001E27190400001F40271A0102271B0102271C020032271D0128271E0102271F010027200102272102015029'
        # binascii_data = '2323C5FE4C45545945454732334C48303134333039010051004F140616111E2D271102000127120155271302000027140F0000000000000000000000000000002715060000000000002716020043271701012718040000001E271904FFFFFFFF271A0102272102015015'

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
        '''发送燃油车车辆实时数据：请求参数：车辆vin码、gateway地址、gateway端口'''

        # binascii_data = '2323C5FE4C45545945454732334C4830313433303901006A0068140616111E2D271102000127120155271302000027140F00FFFFFFFF0000FFFFFFFFFFFFFFFF2715060000000000002716020043271701022718040000001E271904FFFFFFFF271A0102271B0102271C020032271D0128271E0102271F012027200102272102015029'
        # binascii_data = '2323C5FE4C4554454444453138464830303030333301006A00681409090F112C271102050527120144271302000027140F450ABA0AB95432005D005C005B005A2715068070605040302716020043271701022718040000001E271904FFFFFFFF271A0102271B0102271C020032271D0128271E0102271F01202720010227210201501A' # 车门未锁、车门未关、胎压异常
        binascii_data = '2323C5FE4C4554454444453138464830303030333301006A00681409090F112C271102050527120144271302000027140F450ABA0AB95432005D005C005B005A2715068070605040302716020043271701022718040000001E27190400000320271A0102271B0102271C020032271D0128271E0102271F01202720010227210201501A' # 车门未锁、车门未关、胎压异常

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

    def chaichu(self,vin,Longitude,Latitude):
        '''
        拆除报警
        '''
        binascii_data = '232306FE4C455445444445313045483030303030320100111401150F28200001000633F38E01D4067845'
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
        binascii_data = binascii_data.replace(binascii_data[8:42], b2a_hex_vin)  # 替换VIN码
        binascii_data = binascii_data.replace(binascii_data[48:60], now_time)  # 替换时间
        binascii_data = binascii_data.replace(binascii_data[66:74], Longitude)  # 替换经度
        binascii_data = binascii_data.replace(binascii_data[74:82], Latitude)  # 替换纬度
        data = binascii_data[:-2]
        byte1 = int(str(data[0:2]), 16)
        for i in range(len(data) - 2):
            i = i + 2
            if i % 2 == 0:
                byte2 = int(str(data[i:i + 2]), 16)
                byte1 = x_o_r(byte1, byte2)[2:]
                byte1 = int(str(byte1), 16)
        BCC = (hex(byte1)[2:]).upper()
        if len(BCC) == 1:
            BCC = '0' + BCC
        binascii_data = data + BCC
        print(f'拆除报文是:{binascii_data}')
        senddata = binascii.a2b_hex(binascii_data.strip())
        return senddata

if __name__ == '__main__':
    Longitude = get_location.get_Longitude()
    Latitude = get_location.get_Latitude()
    BUFSIZ = 65535
    host = ('192.168.201.135', 31655)  # UAT环境
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
            tcpCliSock.send(lib.terminal_vehicle_realtime_info(vin[i]))
            num = num +1
            mileage = mileage + 5

            if num ==2:
                num = 0
                break
        time.sleep(1)
        # ---------------------------车辆拆除报警-----------------------
        tcpCliSock.send(lib.chaichu(vin[i],Longitude[x],Latitude[x]))
        # ---------------------------------------------------------------
        print("发送车辆熄火")
        tcpCliSock.send(lib.terminal_vehicle_upload_realtime_flameout(vin[i],Longitude[x],Latitude[x],mileage))
        tcpCliSock.send(lib.terminal_vehicle_realtime_info_end(vin[i]))
        time.sleep(0.5)
        print("发送车辆退出登录")
        tcpCliSock.send(lib.terminal_vehicle_logout(vin[i]))
        time.sleep(0.5)
    # logging.info(tcpCliSock.recv(BUFSIZ).decode().strip())
        tcpCliSock.close()
        print ("发送完成")