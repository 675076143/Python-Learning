import re
import requests
import csv
import json
import datetime
startTime = datetime.datetime.now()     # 获取当前时间

listAll = []    # 存放所有数据的列表


def getHTMLText(url,pagenum):
    """
    爬取页面所有数据
    :param url: 要爬取网址的url链接
    :param pagenum: 页码
    :return: 返回爬取到的内容（text）
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            '_fxpcqlniredt': '09031112112144193864'}
        data = json.dumps({
            "pageid": 10650000804,
            "viewid": 140141,
            "tagid": 0,
            "pagenum": pagenum,
            "pagesize": 10,
            "contentType": "json",
            "head":
                {
                    "appid": "100013776",
                    "cid": "09031112112144193864",
                    "ctok": "",
                    "cver": "1.0",
                    "lang": "01",
                    "sid": "8888",
                    "syscode": "09",
                    "auth": "",
                    "extension": []
                },
            "ver": "7.10.3.0319180000"})
        r = requests.post(url,data=data, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "HTTPError异常"


def getComments(i):
    """
    获取每页的评论
    :param i: 页码
    :return:
    """
    text = getHTMLText(url, i)
    text = json.loads(text)
    for j in text["data"]["comments"]:
        data = {"评分": j["score"], "评论": j["content"]}
        listAll.append(data)    # 将该数据添加到listAll中


def getTotalpage(url):
    """
    获取总页数
    :param url: 要爬取网址的url链接
    :return: 总页码
    """
    text = getHTMLText(url, 1)  # 通过获取第一页数据的totalpage数值，来取得总页数
    a = json.loads(text)
    return a["data"]["totalpage"]


if __name__ == "__main__":
    url = "https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList?"
    print("Starting")
    totalPage = getTotalpage(url)
    for i in range(totalPage):  #通过循环 总页数 的次数，获取每一页的数值
        getComments(i)
        process = (i / totalPage) * 100
        print("\r{:^3.0f}%".format(process), end="")

    # 保存文件
    headers = ['评分', '评论']
    with open('20190429.csv', 'w', encoding="utf-8", newline="") as f:
        f_scv = csv.DictWriter(f, headers)
        f_scv.writeheader()
        f_scv.writerows(listAll)
    print("\nDone!")

    endTime = datetime.datetime.now()   #获取当前时间
    print("爬取成功！共耗时：", (endTime - startTime).seconds, "秒")
