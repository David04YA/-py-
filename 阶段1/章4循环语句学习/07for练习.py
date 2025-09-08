#练习：统计一共有多少个英文字母a
name='itheima is a brand of itcast'
count=0
for i in name:
    if i=='a':
        count += 1
print(count)
# 在循环外做一个计数器，用来统计a的个数
# 判断可以用if语句
