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
    
    def __lt__(self, other):
        return self.price<other.price
    
    def __le__(self, other):
        return self.price<=other.price
    
c1=Clock(1,100,"中国")
print(c1)
print(str(c1))


class test:
    def __init__(self):
       print("test")

test()


# __it__数字比较方法
c2=Clock(2,200,"中国")
print(c1<c2)

# __le__小于等于比较方法
print(c1<=c2)

# __eq__等于比较方法 以下不再赘述