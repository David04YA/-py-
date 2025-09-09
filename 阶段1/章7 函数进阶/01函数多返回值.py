# 多个返回值:一个函数要有多个返回值,多个返回值用逗号隔开
def test_return():
    return 1,2,3

x,y,z=test_return()
print(x)
print(y)
print(z) 

# 按照返回值的顺序,写对应顺序的多个变量接收即可