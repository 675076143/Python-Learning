import re
import requests
import csv
import datetime
startTime = datetime.datetime.now()

#爬取网页的通用代码框架

listAll = []

def getHTMLText(url):
    """
    爬取页面所有数据
    :param url: 要爬取网址的url链接
    :return: 返回爬取到的内容（text）
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "HTTPError异常"

def one_cleanout_data(data):
    """
    第一次清洗爬取到的内容
    :param data: 爬取到的所有内容
    :return: 第一次清洗过后的数据(字符串类型)
    """
    data_old = data
    data_list = []  #定义一个列表存放清洗过后的数据
    reg = '<dt>(.*?)</dt>'  # 通过正则表达式获取以<dt>开头 </dt>结尾的内容
    for i in re.findall(reg, data_old, re.S|re.M):
        data_list.append(i) # 将获取到的内容添加到data_list中
    data_list_clean = list(set(data_list))  # 用set清除列表中的重复项

    string_data_list_clean = "" # 定义一个字符串存放清洗过后的数据
    for i in data_list_clean:   # 利用for循环将列表中的内容添加到字符串中
        string_data_list_clean +=i
    return string_data_list_clean

def getMovieDetailUrl(data):
    """
    获取各个电影的详情页链接
    :param data: 第一次清洗过后的数据
    :return: 装有各个电影详情页链接的列表，data_list
    """
    data_old = data
    data_list = []  # 存放所有电影详情页链接的列表
    reg = 'href="(.*?)"'    # 通过正则表达式获取以href="开头 "结尾的数据
    for i in re.findall(reg, data_old): # 通过循环将数据添加到data_list中
        if(i[:1]!="<"):
            data_list.append(i)

    data_list = set(data_list)  # 利用set剔除重复的URL
    return data_list

def getMovieDetail(data,dataUrl):
    """
    获取电影详情，如：
    中文名， 英文名， 导演， 编剧， 评分等
    :param data: 爬取到的各个电影详情页的数据
    :param dataUrl: 各个电影详情页的url链接
    :return: 清洗过后获得的电影详情数据 字典data_dict
    """

    # 电影评分的数据是由AJAX异步请求得到的，链接为下面一大串 + 各个电影详情页的url链接最后7位数字拼接而成
    dataUrl = "http://service.theater.mtime.com/Cinema.api?Ajax_CallBack=true" \
              "&Ajax_CallBackType=Mtime.Cinema.Services" \
              "&Ajax_CallBackMethod=CinemaChannelIndexLoadData" \
              "&Ajax_CrossDomain=1&" \
              "Ajax_RequestUrl=http%3A%2F%2Ftheater.mtime.com%2F" \
              "China_Fujian_Province_Zhangzhou%2F&Ajax_CallBackArgument2="\
              +dataUrl[-7:-1]

    dataSocre = getHTMLText(dataUrl)    # 通过以上链接获取到电影评分
    data_old = data

    # 清洗数据用的正则表达式
    reg5 = '<dl class="info_l">(.*?)</dl>'
    reg12 = '<dd.*?>(.*?)</dd>'
    regHeader = '<h1 .*?>(.*?)</h1>'
    regEngLishName = '<p class="db_enname" style="font-size:25px;">(.*?)</p>'
    regScore = '"Rating":"(.*?)"'
    regImg = '<img src="(.*?)" .*? rel="v:image" />'
    reg13 = '<strong>(.*?)</strong>'
    reg8 = '<a.*?>(.*?)</a>'

    data_dict = {}  # 字典，用于保存清洗过后的数据
    # 清洗数据
    data = re.findall(reg5, data_old, re.S|re.M)
    主要信息 = ""
    for i in data:
        主要信息 = i.replace(" ","")
        主要信息 = 主要信息.replace("：","")
        主要信息 = 主要信息.replace("&#183", "·")
    主要信息 = 主要信息.replace("\r\n","")
    主要信息 = re.findall(reg12, 主要信息)


    # 将清洗得到的数据保存在字典data_dict中
    stringData = ""
    for i in 主要信息:
        for j in re.findall(reg8, i):
            stringData+= j+"，"
        data_dict[re.findall(reg13, i)[0]] = stringData
        stringData = ""
    data_dict["中文名"] = re.findall(regHeader, data_old, re.S | re.M)[0]
    data_dict["英文名"] = re.findall(regEngLishName, data_old, re.S | re.M)[0]
    # 图片名称由 中文名.jpg 而成
    data_dict["图片"] = re.findall(regHeader, data_old, re.S | re.M)[0]+".jpg"
    for i in re.findall(regScore, dataSocre):
        data_dict["评分"] = i
    # 下载电影封面图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    url = re.findall(regImg, data_old, re.S | re.M)[0]
    pic = requests.get(url=url, headers=headers)
    with open(".\images\mtimer\ "+re.findall(regHeader, data_old, re.S | re.M)[0]+".jpg", 'wb') as fp:
        fp.write(pic.content)

    return data_dict

if __name__ == "__main__":
    url = "http://theater.mtime.com/China_Fujian_Province_Zhangzhou/"
    movieDetailUrl = getMovieDetailUrl(one_cleanout_data(getHTMLText(url)))     # 获取电影详情页面的Url链接

    for i in movieDetailUrl:    # 利用for循环访问每个URL链接
        a = getMovieDetail(getHTMLText(i),i)    # 获取每个URL链接页面的数据
        for key2,value2 in a.items():
            print(key2,value2)
        print("------------------------------")
        listAll.append(a)
    # csv文件保存
    headers = ['中文名', '英文名', '导演', '编剧', '国家地区', '制作公司', '发行公司', '更多片名', '评分', '图片']
    with open('20190424.csv', 'w', newline="") as f:
        f_scv = csv.DictWriter(f, headers)
        f_scv.writeheader()
        f_scv.writerows(listAll)

    endTime = datetime.datetime.now()
    print("爬取成功！共耗时：", (endTime - startTime).seconds, "秒")
