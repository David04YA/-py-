# 字符串是字符的容器，一个字符串可以包含多个字符
# 和其他容器一样，字符串也可以用下标来访问

strtest=" itheima and itcast  "
print(strtest[0])
print(strtest[-1])

# 字符串是一个无法修改的容器 修改字符 移除字符 追加字符都无法完成

# 查找功能
# index方法
a = strtest.index("a")
print(a)

#统计功能
# count方法
a2= strtest.count("a")
print(a2)

#字符串的替换方法
# 功能-字符串1全部替换为字符串2 不是修改字符串本身 而是新字符串
new_str=strtest.replace("a","A")
print(new_str)

# 字符串的分割split

strtest2=strtest.split()
print(strtest2)
print(type(strtest2))

# 字符串的规整strip

strtest3=strtest.strip()
print(strtest3)

# strip有默认值，留空就默认移除空格
# 也可以指定移除的字符
str="1234567890"
str4=str.strip("1234567890")
print(str4)


# 统计长度
str5=len(strtest)
print(str5)

# 字符串有以下特点：
# 1.字符串是字符的容器
# 2.字符串是有序的
# 3.字符串是不可修改的
# 4.允许重复