#condig:utf-8

class Calculater:
    is_raise = False
    def calc(self,express):
        try:
            return eval(express)
        except ZeroDivisionError:
            if self.is_raise:
                return "Zero can no be division"
            else:
                raise

if __name__=="__main__":
    c = Calculater()
    c.is_raise = True
    print(c.calc("8/0"))
