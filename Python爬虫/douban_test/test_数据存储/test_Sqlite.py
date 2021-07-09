import sqlite3

#1,连接数据库
# coon =sqlite3.connect("test.db")    #打开或创建数据库
#
# print("Opende database successfully")

'''
#2,创建数据表
coon = sqlite3.connect("test.db")
print("成功打开数据库")

c = coon.cursor()       #获取游标
'''
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary REAL);
# '''
'''

c.execute(sql)          #执行SQL语句
coon.commit()           #提交数据库操作
coon.close()            #关闭数据库连接

print("成功建表")
'''


# #3,插入数据
# coon = sqlite3.connect("test.db")
# print("成功打开数据库")
#
# c = coon.cursor()       #获取游标
#
# sql1 = '''
#     insert into company(id,name,age,address,salary)
#       VALUES (1,'张三',32,"成都",8000);
# '''
#
# sql2 = '''
#     insert into company(id,name,age,address,salary)
#       VALUES (2,'李四',25,"南京",10000);
# '''
#
#
# c.execute(sql1)          #执行SQL语句
# c.execute(sql2)          #执行SQL语句
# coon.commit()           #提交数据库操作
# coon.close()            #关闭数据库连接
#
# print("插入数据完毕")

#4,查询数据
coon = sqlite3.connect("test.db")
print("成功打开数据库")

c = coon.cursor()       #获取游标

sql = "select id,name,address,salary from company"


cursor = c.execute(sql)          #执行SQL语句

for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3],"\n")

coon.close()            #关闭数据库连接

print("查询数据完毕")