#coding:utf-8
'''
16. 有一只猴子，摘得了一些桃子。它第一天吃掉了所有桃子的一半，还不瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，再吃了一个。以后每天都吃了前一天剩下的一半并多一个。到第10天想再吃桃子时，发见只剩下一个了。编写程序，计算曾经这只猴子总共摘得了多少只桃子。
'''

x2 = 1
for day in range(9, 0, -1):
    x1 = (x2 + 1) * 2
    x2 = x1
print(x1)