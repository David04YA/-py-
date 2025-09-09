# 位置参数:调用函数时,根据函数定义的参数位置,传递参数

def user_info(name,age,gender):
    print(f"我是{name},我今年{age}岁,我是{gender}")

user_info("张三",18,"男")

# 关键字参数:调用函数时,根据函数定义的参数名称,传递参数
# 可以与位置参数混用,位置参数必须在前,且匹配参数顺序

def user_info2(name,age,gender):
    print(f"名字是{name},年龄是{age},性别是{gender}")

user_info2(name="张三",age=18,gender="男")

user_info2(age=18,name="张三",gender="男")

user_info2("张三",age=18,gender="男")

# 缺省参数:调用函数时,没有传递参数,则使用默认值

def user_info3(name,age,gender="男"):
    print(f"名字是{name},年龄是{age},性别是{gender}")

user_info3("张三",18)


# 不定长参数(可变参数) 
# 调用函数时,可以传递任意个参数,参数数量不限
# 定义函数时,可以使用*args来接收不定长参数
# args是一个元组,可以使用元组的方法来操作
def test_args(*args):
    print(args)

test_args(1,2,3)
test_args(1,2,3,4,5,6)

# 当使用不定长参数时,args是一个元组,可以存储任意个元素


def test_args2(**kwargs):
    print(kwargs)

print(test_args2(name="张三",age=18,gender="男"))
# 参数是键值对的情况下,所有键值对都会被kwargs接收,同时形成字典
# 不定长参数最大特点 *