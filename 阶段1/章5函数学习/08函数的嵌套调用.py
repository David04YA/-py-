# 函数嵌套调用：一个函数里面调用另一个函数

def func_b():
    print("func_b被调用了")
    return "hello"

def func_a():
    print("func_a被调用了")
    func_b()
    return "world"


func_a()

# 函数A执行中调用了函数B，会将函数B全部执行


# 变量作用域-全局变量和局部变量
# 全局变量：在函数外部定义的变量，在函数内部和外部都可以使用
# 局部变量：在函数内部定义的变量，只能在函数内部使用

def test():
    a = 10  # 局部变量
    print(a)

test()
# print(a)  # 报错，a在函数外部无法访问

num=100
def demo():
    print(num)  # 可以访问全局变量num
print(num)  # 可以访问全局变量num
demo() 