import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/basetrans'
data = {
    'from':'ch',
    'to':'en',
    'transtype':'translang',
    'query':'责任',
    'simple_mians_flag':'3',
}
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
}
data = urllib.parse.urlencode(data)
data = data.encode()
request = urllib.request.Request(url = url ,headers = headers)
response = urllib.request.urlopen(request, data = data)
print(response.read())