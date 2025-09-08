# 返回值会将相加的结果返回给函数调用者

# 变量= 函数（参数）

def my_len(s):
    count=0
    for i in s:
        count += 1
    return count

r= my_len("hello")
print(r)    