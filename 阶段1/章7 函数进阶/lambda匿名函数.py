# 有名称的函数可以重复使用 无名称的lambda函数只能使用一次
# lambda 传入参数: 函数体 函数体只能写一行

def test(func):
    print(func(1,2))

test(lambda a,b:a+b )