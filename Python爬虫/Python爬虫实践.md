# Python爬虫

## 1.任务介绍

**需求分析**

爬取豆瓣电影Top250的基本信息，包括电影的名称、豆瓣评分、评价数、电影概括、电影链接等。

https://movie.douban.com/top250

## 2.爬虫初识

**什么是爬虫**

网络爬虫，是一种按照一定规则，自动抓取互联网信息的程序或者脚本。由于互联网数据的多样性和资源的有限性，根据用户需求定向抓取相关网页并分析已成为如今主流的爬取策略。

**爬虫可以做什么**

可以爬取图片、视频等，只要能通过浏览器访问的数据都可以爬取。

**爬虫的本质是什么**

模拟浏览器打开网页，获取网页中我们想要的那部分数据。

## 3.基本流程

**1.准备工作**

通过浏览器查看分析目标网页，学习编程基础规范

**2.获取数据**

通过HTTP库向目标站点发送请求，请求可以包含额外的header等信息，如果服务器能正常响应，会得到一个Response，便是所要获取的页面内容。

**3.解析内容**

得到的内容可能是HTML、json等格式，可以用页面解析库、正则表达式等进行解析。

**4.保存数据**

保存形式多样，可以存为文本格式，也可以保存到数据库，或者保存特定格式的文件。

### 3.1准备工作

#### 3.1.1 URL分析

https://movie.douban.com/top250?start=0;	https://movie.douban.com/top250?start=25

#### 3.1.2 页面分析

借助Chrome开发者工具（F12）来分析网页，在Elements下找到需要的数据位置

#### 3.1.3 编码规范

Python文件中可以加入main函数用于测试程序

```python
if __name__ == "__main__":
```

#### 3.1.4引入模块

```python

import bs4 #网页解析，获取数据
from bs4 import BeautifulSoup
import re  #正则表达式，进行文字匹配
import urllib.request,urllib.error #指定URL，获取网页数据
import xlwt	#进行excel操作
import sqlite3 #进行SQLite数据库操作
```



```python
def main():
    print("开始爬取。。。。")
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = getData(baseurl)
    savepath = u'/home/aistudio/data/豆瓣电影top250.xls'
    saveData(datalist,savepath)
    
    main()
    print("爬取完成。。。。")
```

### 3.2获取数据

```python
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

    return html
```



### 3.3解析内容

**对爬取的HTML文件进行解析**



#### 3.3.1标签解析





#### 3.3.2正则提取







### 3.4保存数据













## 正则表达式的常用操作符

| **操作符** | **说明**                            | **实例**                                    |
| ---------- | ----------------------------------- | ------------------------------------------- |
| .          | 表示任何单个字符                    |                                             |
| [ ]        | 字符集，对单个字符给出取值范围      | [abc]表示a、b、c,[a-z]表示a到z单个字符      |
| [^ ]       | 非字符集，对单个字符给出排除范围    | [^abc]表示非a或b或c的单个字符               |
| *          | 前一个字符0次或无限次扩展           | abc* 表示ab、abc、abcc、abccc等             |
| +          | 前一个字符1次或无限次扩展           | abc+ 表示abc、abcc、abccc等                 |
| ?          | 前一个字符0次或1次扩展              | abc? 表示ab、abc                            |
| \|         | 左右表达式任意一个                  | abc \| abf表示 abc、abf                     |
| {m}        | 扩展前一个字符 m 次                 | ab{2}c 表示 abbc                            |
| {m,n}      | 扩展前一个字符 m 至 n 次（含 n 次） | ab{1，2}c 表示abc，abbc                     |
| ^          | 匹配字符串开头                      | ^abc 表示 abc 且在一个字符串的开头          |
| $          | 匹配字符串结尾                      | abc$表示 abc 且在一个字符串的结尾           |
| ()         | 分组标记，内部只能使用              | abc）表示 abc，（abc \|  def）表示 abc，def |
| \d         | 数字                                | 等价于[0-9]                                 |
| \w         | 单词字符                            | 等价于[A-Za-z0-9_]                          |
| ————       |                                     |                                             |

## Re库的主要功能函数

| 函数          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| re.search()   | 在一个字符串搜索匹配正则表达式的第一个位置，返回match对象    |
| re.match()    | 从一个字符串的开始位置起匹配正则表达式，返回match对象        |
| re.findall()  | 搜索字符串，以列表类型返回全部能匹配的子串                   |
| re.split()    | 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型     |
| re.finditer() | 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象 |
| re.sub()      | 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串 |
|               |                                                              |

正则表达式可以包含一些可选标志修饰符来控制匹配的模式，修饰符被指定为一个可选的标志，多个标志可以通过按位 OR(|)它们来指定，如 re.I | re.M 被设置成 I 和 M 标志。

| 修饰符 | 描述                                                       |
| ------ | ---------------------------------------------------------- |
| re.l   | 使匹配对大小写不敏感                                       |
| re.L   | 做本地化识别(local-aware)匹配                              |
| re.M   | 多行匹配，影响^ 和 $                                       |
| re.S   | 使用 . 匹配包括换行在内的所有字符                          |
| re.U   | 根据Unicode字符集解析字符。这个标志影响\w,\W,\b,\B         |
| re.X   | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易理解 |
|        |                                                            |

