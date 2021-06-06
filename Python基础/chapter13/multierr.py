#coding:utf-8

while True:
    try:
        a = float(input('first number:'))
        b = float(input('second number:'))
        r = a / b
        print("{0} / {1} = {2}".format(a,b,r))
        break
    except ZeroDivisionError:
        print("The second numbers can not be zero.Try again.")
    except ValueError:
        print("Please enter number.Try again.")
    except:
        break
    