# 1.模块的导入
# 什么是模块

# 模块是一个py文件,模块中可以定义函数,类,变量,常量等 py中有不同的模块,一个模块就是一个工具包
# 模块的导入语法 [from 模块名] import [模块中的函数,类,变量,常量
# 常见语法 import 模块名1,模块名2

import time #导入time模块 time.pyi
print("你好")
time.sleep(5)  # 通过导入模块,可以使用模块内部全部的函数,类,变量,常量

print("我好")

from time import sleep


# 2.自定义模块

# 如何制作自定义模块并使用
# 1.创建一个py文件,文件名就是模块名
# 2.在py文件中定义函数,类,变量,常量等
# 3.在其他py文件中导入自定义模块
from modetest1 import test
test(1,2)

# 导入不同模块的同名功能
from modetest2 import test
test(1,2)

# 后面会覆盖前面

#  from的时候会导入整个模块,可以使用模块中的所有内容,同时会直接执行模块内的内容

# 如果一个模块中有__all__变量 使用from 模块名 import *  只能导入_all_变量中的内容 这个变量控制了*时哪些功能可以被导入


from modetest2 import *
