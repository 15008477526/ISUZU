'''

获取经纬度

'''
def get_list():
    locations=[]
    # with open("C:\\Users\\windows-pc\\Desktop\\wjl\\ttt.txt", 'r') as file:
    # with open("C:\\Users\\windows-pc\\Desktop\\wjl\\ttt2.txt", 'r') as file:
    # with open("C:\\Users\\windows-pc\\Desktop\\wjl\\nanchang.txt", 'r') as file:
    with open("C:\\Users\\windows-pc\\Desktop\\wjl\\dongmenbridge.txt", 'r') as file:
        while True:
            line = file.readline()[:-1] #去掉换行符
            if line is not "":
                locations.append(line.split(",", 1))
            if not line:
                break
    # print (locations)
    return locations

def get_Longitude():  #经度
    list = get_list()
    Longitude = []
    for i in list:
        data = i[0].replace(".", "")
        if i[0].index('.')==2:
            for i in range(1, 8):
                if (len(data)) == i:
                    i = (8 - i) * str(0)
                    data = data + i
                    break
        else:
            for i in range(1,9):
                if (len(data)) == i:
                    i = (9 - i) * str(0)
                    data = data + i
                    break
        data = hex(int(data))[2:].upper()
        for i in range(1,8):
            if (len(data)) == i:
                i = (8 - i) * str(0)
                data = i + data
                break
        Longitude.append(data)
    # print (Longitude)
    return Longitude

def get_Latitude():  #纬度
    list = get_list()
    Latitude = []
    for i in list:
        data = i[1].replace(".", "")
        for i in range(1,8):
            if (len(data)) == i:
                i = (8 - i) * str(0)
                data = data + i
                break
        data = hex(int(data))[2:].upper()
        for i in range(1,8):
            if (len(data)) == i:
                i = (8 - i) * str(0)
                data = i + data
                break
        Latitude.append(data)
    # print(Latitude)
    return Latitude



# if __name__=="__main__":
    # a = get_Longitude()
    #
    # print (a)
