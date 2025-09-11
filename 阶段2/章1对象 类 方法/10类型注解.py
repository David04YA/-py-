# 在自定义函数和方法中给参数注明类型
# 注解:对变量类型进行注解 对函数形参和返回值的类型进行注解

# 基础数据类型注解
var_1:int 
var_2:float

# 类对象类型注解
class student:
    pass
stu:student=student()


# 基础类容器类型注解:
my_list:list

# 以此类推


# union类型注解
from typing import Union
list:list[Union[str,int]]
# 指的是既可以传入strIng,也可以传入int