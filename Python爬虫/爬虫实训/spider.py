import urllib.request,urllib.error #指定URL，获取网页数据

def main():
    askURL("https://movie.douban.com/top250?start=0")

#得到指定一个URL的网页内容
def askURL(url):
    head = {    #模拟浏览器头部信息，向豆瓣服务器发送消息
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
    }   #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接收什么水平的文字）

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

if __name__ == "__main__":
    main()