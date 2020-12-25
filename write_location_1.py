'''
写入行程经纬度
'''
import requests
import json

# url='https://restapi.amap.com/v4/direction/truck?origin=115.816675,28.692068&originid=undefined&originidtype=undefined&destination=115.880463,28.713101&destinationid=undefined&destinationtype=undefined&s=rsv3&strategy=0&key=c23237b8dcdd6309f0329cd5e78f09d2&size=1&width=2.5&height=2&load=1&weight=12&axis=2&callback=jsonp_294776_&platform=JS&logversion=2.0&appname=http%3A%2F%2Flocalhost%3A63342%2Fisuzu%2Fget_location.html%3F_ijt%3Dblj8srku97sm9edtvcgltfpd46&csid=BC88D50C-7DE4-4C30-94F4-1C920C183DE9&sdkversion=1.4.11'
url='https://restapi.amap.com/v4/direction/truck?origin=104.087308,30.648192&originid=&originidtype=&destination=104.075933,30.637421&destinationid=&destinationtype=&s=rsv3&strategy=0&key=c23237b8dcdd6309f0329cd5e78f09d2&size=1&width=2.5&height=2&load=1&weight=12&axis=2&callback=jsonp_746431_&platform=JS&logversion=2.0&appname=file%3A%2F%2F%2FE%3A%2Fpython%2Fisuzu%2Fget_location.html&csid=E67CAD84-EB28-44B5-89B9-81BC3E7E9EB1&sdkversion=1.4.15'
# url='https://restapi.amap.com/v4/direction/truck?origin=104.137038,30.666147&originid=undefined&originidtype=undefined&destination=104.029878,30.634704&destinationid=undefined&destinationtype=undefined&s=rsv3&strategy=0&key=c23237b8dcdd6309f0329cd5e78f09d2&size=1&width=2.5&height=2&load=1&weight=12&axis=2&callback=jsonp_430348_&platform=JS&logversion=2.0&appname=http%3A%2F%2Flocalhost%3A63342%2Fisuzu%2Fget_location.html%3F_ijt%3Dh6rce3colegd1k84r60i31prg3&csid=F43A71E8-97FE-4132-924A-193AC6B69AE3&sdkversion=1.4.11'
response = requests.get(url=url,verify=False)
print(response)
response_json = response.text[14:-1]
steps = json.loads(response_json)
steps = steps['data']['route']['paths'][0]['steps']
# print (len(steps))
location_list =[]
# f = open("C:\\Users\\windows-pc\\Desktop\\wjl\\ttt.txt",'w')
# f = open("C:\\Users\\windows-pc\\Desktop\\wjl\\nanchang.txt",'w')
f = open("C:\\Users\\windows-pc\\Desktop\\wjl\\dongmenbridge.txt",'w')
for step in steps:
    # print (step['polyline'].replace(';','\n'))
    f.write(step['polyline'].replace(';','\n') + '\n')
    # location_list.append(step['polyline'].replace(';',' '))
# print (location_list)
print ("写入完成")
f.close()