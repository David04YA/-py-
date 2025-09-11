# 多态：指的是多种状态，完成某个行为时，使用不同的对象会有不同的状态

class Animal:
    def sepak(self):
        pass

# 父类的speak方法是空实现，子类可以根据需要复写该方法
# 父类确定有哪些方法，具体实现靠子类，这种写法就是抽象类，方法体是空实现的方法称为抽象方法
class Dog(Animal):
    def sepak(self):
        print("汪汪")

class Cat(Animal):
    def sepak(self):
        print("喵喵")

def make_sepak(animal:Animal):
    animal.sepak()  
# 多态的实现：
# 1. 继承
# 2. 复写
# 3. 父类引用指向子类对象

dog=Dog()
cat=Cat()

make_sepak(dog)
make_sepak(cat) 
# 抽象类 (接口)

class AC:
    def cold(self):
        pass
    def hot(self):
        pass
    def fan(self):
        pass

class midea_AC(AC):
    def cold(self):
        print("制冷")
    def hot(self):
        print("制热")
    def fan(self):
        print("通风")
    def swing(self):
        print("摆风")
def make_cold(ac:AC):
    ac.cold()

make_cold(midea_AC())