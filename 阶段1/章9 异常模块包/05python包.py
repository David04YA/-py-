# 1什么是包
# 从物理上 包就是一个文件夹,包含了任意多模块和一个 _init_.py文件 从逻辑上 包就是一个模块

import package.mode1
package.mode1.test1()

# 也可以通过from语句来导入

from package import mode1
from package.mode1 import test1

from package import *
# 包的*也和模块一样,要提前写好__all__变量

