# __init__构造方法，就是其中一个内置方法 内置方法也可以叫做魔术方法

# __str__字符串方法 当使用print输出对象的时候本来默认输出内存地址，用__str__方法，让其输出字符串

class Clock:
    id=None
    price=None
    brand=None
    def __init__(self,id,price,brand):
        self.id=id
        self.price=price
        self.brand=brand
    def __str__(self):
        return f"我是一个时钟，我的id是{self.id},我的价格是{self.price},我的品牌是{self.brand}"
    
c1=Clock(1,100,"中国")
print(c1)
print(str(c1))


class test:
    def __init__(self):
       return "test"

t=test()
print(t)


# __it__数字比较方法

cl