import xlwt

'''
workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象   文件
worksheet = workbook.add_sheet('sheet1')    #文件中的表单,创建工作表
worksheet.write(0,0,'hello')    #写入数据，第一行参数“行”, 第二行参数“列”,第三个参数内容
workbook.save('student.xls')    #保存数据表
'''

#将九九乘法表写入Excel
workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象   文件
worksheet = workbook.add_sheet('sheet1')    #文件中的表单,创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')