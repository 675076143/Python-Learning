import re
import requests
import multiprocessing
import csv
import datetime
starttime = datetime.datetime.now()

#爬取网页的通用代码框架

listAll = []

def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "HTTPError异常"

def one_cleanout_data(data):    #第一次清洗dt标签中的内容
    data_old = data
    num = 1
    data_list = []
    reg3 = '<dt>(.*?)</dt>'
    #pattern = re.compile(reg)

    #for i in re.findall(r'<img src=".*?[^/>|^>]/>', data_old):
    for i in re.findall(reg3, data_old, re.S|re.M):
        data_list.append(i)
        #print('计数：%d，数据清洗成功:%s' % (num, i))
        num += 1

    j = 0
    data_list_clean = list(set(data_list))
    string_data_list_clean = ""
    for i in data_list_clean:
        j+=1
        print(j,": ",i)
        string_data_list_clean +=i
    return string_data_list_clean

def getMovieName(data):     #获取电影名
    data_old = data
    num = 1
    data_list = []
    reg3 = '<a .*?>(.*?)</a>'
    for i in re.findall(reg3, data_old, re.S|re.M):
        if(i[:1]!="<"):
            movieDict = {"电影名称：":i}
            #print(movieDict)
            data_list.append(movieDict)
            #print('计数：%d，数据清洗成功:%s' % (num, i))
            num += 1


    return data_list

def getMovieDetailUrl(data):
    data_old = data
    num = 1
    data_list = []
    reg = 'href="(.*?)"'
    for i in re.findall(reg, data_old):
        if(i[:1]!="<"):
            data_list.append(i)
            num += 1

    data_list = set(data_list)  #剔除重复的URL
    return data_list

def getMovieDetail(data,dataUrl):
    dataUrl = "http://service.theater.mtime.com/Cinema.api?Ajax_CallBack=true" \
              "&Ajax_CallBackType=Mtime.Cinema.Services" \
              "&Ajax_CallBackMethod=CinemaChannelIndexLoadData" \
              "&Ajax_CrossDomain=1&" \
              "Ajax_RequestUrl=http%3A%2F%2Ftheater.mtime.com%2F" \
              "China_Fujian_Province_Zhangzhou%2F&Ajax_CallBackArgument2="\
              +dataUrl[-7:-1]

    dataSocre = getHTMLText(dataUrl)
    data_old = data
    reg5 = '<dl class="info_l">(.*?)</dl>'
    reg12 = '<dd.*?>(.*?)</dd>'
    regHeader = '<h1 .*?>(.*?)</h1>'
    regEngLishName = '<p class="db_enname" style="font-size:25px;">(.*?)</p>'
    regScore = '"Rating":"(.*?)"'
    data_dict = {}

    data = re.findall(reg5, data_old, re.S|re.M)
    主要信息 = ""

    for i in data:
        主要信息 = i.replace(" ","")
        主要信息 = 主要信息.replace("：","")
    主要信息 = 主要信息.replace("\r\n","")
    主要信息 = re.findall(reg12, 主要信息)


    reg13 = '<strong>(.*?)</strong>'
    reg8 = '<a.*?>(.*?)</a>'
    stringData = ""
    for i in 主要信息:
        for j in re.findall(reg8, i):
            stringData+= j+"，"
        data_dict[re.findall(reg13, i)[0]] = stringData
        stringData = ""
    data_dict["中文名"] = re.findall(regHeader, data_old, re.S | re.M)[0]
    data_dict["英文名"] = re.findall(regEngLishName, data_old, re.S | re.M)[0]
    for i in re.findall(regScore,dataSocre):
        data_dict["评分"] = i
    return data_dict

def getMovieDetail_two(data):
    data_old = data
    data_dict = {}
    reg13 = '<strong>(.*?)</strong>'
    reg8 = '<a.*?>(.*?)</a>'
    for i in data_old:
        data_dict[re.findall(reg13, i)[0]] = re.findall(reg8, i)

    return data_dict

if __name__ == "__main__":
    url = "http://theater.mtime.com/China_Fujian_Province_Zhangzhou/"
    movieDetailUrl = getMovieDetailUrl(one_cleanout_data(getHTMLText(url)))

    for i in movieDetailUrl:
        a = getMovieDetail(getHTMLText(i),i)
        for key2,value2 in a.items():
            print(key2,value2)
        print("------------------------------")
        listAll.append(a)

    headers = ['中文名', '英文名', '导演', '编剧', '国家地区', '制作公司', '发行公司', '更多片名', '评分']
    with open('20190424.csv', 'w', newline="") as f:
        f_scv = csv.DictWriter(f, headers)
        f_scv.writeheader()
        f_scv.writerows(listAll)
    # print(listAll)
    endtime = datetime.datetime.now()
    print("爬取成功！共耗时：", (endtime - starttime).seconds, "秒")
