# 子类继承父类的属性和方法后,可以进行复写,重新定义同名属性和方法
class phone:
    IMEI =  None
    producer="HH"

    def call_by_4g(self):
        print("正在通话中")


class test(phone):
    
    producer="HH2"
    IMEI="1234567890"
    def call_by_4g(self):
        return super().call_by_4g()

# 一旦复写,调用成员时默认调用复写后的
# 如果要使用被复写的父类的方法,可以使用super() 或者父类名.成员变量/成员方法

test=test()
test.call_by_4g()
print(test.producer)
