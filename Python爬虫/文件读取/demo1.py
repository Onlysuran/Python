
'''
f = open("test.txt","w") #打开文件·w模式(写模式)，文件不存在就新建

f.write("hello word,i am here!") #将字符串写入文件中

f.close() #关闭文件
'''




'''
#read方法，读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定的字符数

f = open("test.txt","r")

content = f.read(5)
print(content)

content = f.read(10)
print(content)

f.close()
'''

from contextlib import contextmanager
from os import read
import os

'''
f = open("test.txt","r")

content = f.readlines()     #一次性读取全部文件为列表，每行一个字符串元素
print(content)

i= 1 #定义一个行号
for temp in content:
    print("%d:%s"%(i,temp)) #第几行%d，第一行的内容%s，%占位，i行号，temp内容
    i += 1

f.close()
'''

'''
f = open("test.txt","r")

content = f.readline()
print("1:%s"%content,end="")

conternt = f.readline()
print("2:%s"%content,end="")

f.close()
'''

'''
OS 模块中的rename()可以完成对文件的重命名操作
os.rename(需要修改的文件名，新的文件名)

OS 模块中的remove()可以完成对文件的删除操作
os.remove(待删除的文件名)

os.mkdir("创建文件夹")
os.getcwd() #获取当前目录
os.chdir("../") #改变默认目录
os.listdir("./") #获取目录列表
os.rmdir("文件夹") #删除文件夹
'''

import os
os.rename("test1.txt","test_文件读取.txt")