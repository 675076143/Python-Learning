import requests

#爬取网页的通用代码框架
def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "HTTPError异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))