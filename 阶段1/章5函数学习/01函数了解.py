# 函数：写好的，可以重复使用的代码块
# 函数的作用：封装代码，重复使用
# 函数的分类：
# 1.系统函数：python自带的函数，例如print()、input()、range()等
# 2.自定义函数：由程序员自己定义的函数  

#需求：统计字符串长度，不适用内置函数len

count=0
for i in 'itheima':
    count += 1
print(count)

# 定义函数
# def 函数名():
#     函数体
#     return 函数返回值

def my_len(s):
    count=0
    for i in s:
        count += 1
    return count    

# 调用函数

print(my_len('itheima is a brand of itcast'))