# 需求：随机猜数字 无限次机会，直到猜中为止
# 猜完后提示猜了几次 --- 需要一个计数器

import random 
num=random.randint(1,100)

#定义一个布尔类型的变量
flag = True
count = 0
while flag:
    guess = int(input("请输入你猜想的数字:"))
    count += 1
    if guess==num:
       print("恭喜你猜对了，你一共猜了%d次" % count)
       flag=False
    else:
       if guess > num:
           print("你猜的数字大了")
       else:
           print("你猜的数字小了")
print("游戏结束，你一共猜了%d次" % count)
