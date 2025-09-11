# 类的使用语法 类名():
# 类的属性 （成员变量）
# 类的行为 （成员方法） 类里就两个，数据 方法

# 以下是方法演示

class Student:
    name=None
    age=None
    sex=None
    def say_hello(self):
        print("你好")

    # 获取类的具体对象 调用类内部的函数

stu=Student()
stu.name="张三"
stu.age=18
stu.sex="男"
stu.say_hello()

# 成员方法和定义函数基本一致，只是成员方法第一个参数必须是self
# def 方法名（self,参数1,参数2）:
#     方法体
# 在方法内部，想访问类的成员变量，必须用self


