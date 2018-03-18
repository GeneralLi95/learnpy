from flask import Flask
from flask import request
import json as js
import re
from urllib.request import urlopen

app = Flask(__name__)

def getdata(url):                    #直接从url地址获取数据的函数
    textPage = urlopen(url)
    a = textPage.read().decode('utf-8')    #read数据是没有解码的，要加一个解码decode
    return js.loads(a)

@app.route('/')
def hello_world():
    url = "http://119.23.74.200:8888/Weather/GetList?date=20180310&hour=11"
    cfl = getdata(url)

    code_loc = open('stcode_loc.txt', 'r')  # 存储站点编号和位置的文件，txt格式，分号隔开，split函数把隔开
    #如果路径有问题，则将stcode_loc.txt路径改为绝对路径
    lines = code_loc.readlines()

    num = len(cfl['table'])  # 读取Table关键字的长度   即上报火情级别的站点数目
    # code_sum = [[0] * 3] * num
    # #数组的定义容易犯错的一个地方,这样做会导致二维数组中的量同时发生变化，应该采用下面的定义方法
    code_sum = [([0] * 3) for i in range(len(lines))]

    for i, line in enumerate(lines):
        p = re.split('[;]', line)  # 使用一个正则模块对每一行进行切割line  line中的信息分别为  序号；名称；编号；经度；纬度
        # print(p[2],p[3],p[4])
        code_sum[i][0] = round(float(p[4]), 2)  # p(4）纬度放第一位 round函数使保留两位小数
        code_sum[i][1] = float(p[3])  # p(3) 经度放第二位
        code_sum[i][2] = '0'  # 第三位 火情信息，默认为0，有反馈的站点信息更新
        for st in cfl['table']:
            if p[2][1:-1] == st['code']:
                code_sum[i][2] = repr(st['firelevel'] * 500)
                break
                #  print (code_sum[i],end='')
                #  if i<157 :
                #      print(",")

    print("var addressPoints =",code_sum,";")

    return  "var addressPoints = "+"%s" % code_sum + ";"



if __name__ == '__main__':
    app.debug = True    #开启调试功能
    app.run()
