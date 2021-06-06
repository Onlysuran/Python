#coding:utf-8
'''
常用的文件打开方式：
r:以读的方式打开文件。默认打开模式
w:以写的方式打开文件。如果文件已经存在，则覆盖源文件，否则新建文件
a:以写的方式打开文件。如果文件已经存在，则指针在文件的最后，实现向文件中追加新内容；否则，新建文件
b:以二进制模式打开文件。不单独使用，配合r/w/a等模式使用
+:同时实现读写操作。不单独使用，配合r/w/a等模式使用
x:创建文件，但如果文件存在，则无法创建
'''
'''
import os

f = open("test.txt","w")
f.write('Life is short, You need Python')
f.close()

f = open('test.txt')
print(f.read())
'''

import csv
data = [['name','number'],['Python','111'],['Java','222'],['PHP','333']]
with open('csvfile.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
f = open('csvfile.csv')
reader = csv.reader(f)
for row in reader:
    print(row) 