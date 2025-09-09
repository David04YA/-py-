# 1.函数作为参数传递 
# 在前面的函数学习中，我们一直接收数据来传入，但其实也可以把函数自身传入函数内


def test(func):
    print(func)


def func(a,b):
    return a+b

test(func(1,2))

# 这是一种计算逻辑的传递，而不是数据的传递 在test函数中，由传入的func函数，完成了它的计算操作

