#condig:utf-8
#装饰器函数
class Fibs:
    def __init__(self,max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a+self.b
        return fib

fibs = Fibs(1000000)
lst = [fibs.__next__() for i in range(10)]
print(lst)


#生成器函数
def fibs():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr 
import itertools
print(list(itertools.islice(fibs(), 10 )))

gt = [x**2 for x in range(10)]
print(gt)