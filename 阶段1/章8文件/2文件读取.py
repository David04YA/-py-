# 操作系统以文件的形式管理数据
# 打开文件 open函数 open(name,mode,encoding)
# name 文件名
# mode 打开模式 r只读 w写入 a追加
# encoding 编码
f = open('test.txt','r',encoding='utf-8')
# f是open函数的文件对象

# read()方法：从文件中读取数据的字节长度，如果没有指定长度，默认读取文件所有内容

# 读取文件内容
content = f.read(10)
print(content)

# readlines()方法：读取文件所有内容，返回一个列表，每个元素是文件的一行

# 读取文件所有内容  \n换行
content = f.readlines()
print(content)

# 文件有指针，重复读取不会从头开始

# readline()方法：读取文件一行内容
# 读取文件一行内容
content = f.readline()
print(content)
content2 = f.readline()
print(content2) 

# for循环读取 
for line in f:
    print(line)


# 关闭文件
f.close()

import time
time.sleep(1)  #文件休眠


# with open语法 
with open('test.txt','r',encoding='utf-8') as f:
 for line in f:
    print(line)

# with open语法完成后，文件会自动关闭