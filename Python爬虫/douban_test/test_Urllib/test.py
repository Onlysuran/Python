import urllib.request

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))#对获取到的网页源码进行utf-8解码


#获取一个post请求
#测试网站http://httpbin.org

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"word"}),encoding="utf-8")  #转化成二进制的数据包
#
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))


#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out")



# response = urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)#状态码
# print(response.getheader("Server"))


# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
# }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))


url = "https://www.douban.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
}
data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))





