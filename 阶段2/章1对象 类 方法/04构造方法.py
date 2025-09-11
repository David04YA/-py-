# 构造方法 __init__ 这个__init__ 是一个特殊的方法，当创建一个对象时，会自动调用这个方法

class Clock:
    id=None
    price=None
    brand=None
    def __init__(self,id,price,brand):
        self.id=id
        self.price=price
        self.brand=brand

clock=Clock(1,100,"中国")