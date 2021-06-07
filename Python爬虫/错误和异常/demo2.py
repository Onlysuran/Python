
#try.....finally  和嵌套
 
import time
try:
    f = open("test_文件读取.txt","r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")



except Exception as result:
    print("发生异常。。。")

